import webbrowser

import spotipy
from furl import furl
from playlist_kreator.providers.base import BaseProvider


# This is the playlist-kreator app client id, we don't need the secret, as we do client side auth
SPOTIFY_CLIENT_ID = 'b1c5cfc647d146e0955db636cf387132'


class SpotifyProvider(BaseProvider):
    def get_artist_id(self, artist_name):
        result = self.spotify_api.search(artist_name, limit=1, type='artist')
        if len(result['artists']['items']) == 0:
            return None

        return result['artists']['items'][0]['id']

    def get_artist_top_song_ids(self, artist_id, max_top_tracks):
        top_tracks = self.spotify_api.artist_top_tracks(artist_id)
        return [track['id'] for track in top_tracks['tracks'][:max_top_tracks]]

    def create_playlist(self, playlist_name):
        username = self.user_info['username']
        playlist = self.spotify_api.user_playlist_create(username, playlist_name)
        return playlist['id']

    def add_songs_to_playlist(self, playlist_id, song_ids):
        username = self.user_info['username']
        max_tracks_per_request = 100
        i = 0
        nb_tracks = len(song_ids)
        while i * max_tracks_per_request < nb_tracks:
            subsong_ids = song_ids[i * max_tracks_per_request:i * max_tracks_per_request + max_tracks_per_request]
            self.spotify_api.user_playlist_add_tracks(username, playlist_id, subsong_ids)
            i += 1

    def get_user_info(self, args):
        username = args.username
        if username:
            print("Username: {}".format(username))
        else:
            print(
                "You will need your spotify username. You can get it from: https://www.spotify.com/us/account/overview/")
            username = input("Username: ")

        auth_url = self._get_auth_url()
        webbrowser.open(auth_url)

        print('''
                User authentication requires interaction with your
                web browser.
                This will open a page in your browser.
                Paste that url you were directed to to
                complete the authorization.
            ''')

        redirect_url = input('Enter the URL you were redirected to: ')
        # Why #??
        redirect_furl = furl(redirect_url.replace('callback/#access_token', 'callback/?access_token'))
        token = redirect_furl.args['access_token']

        self.user_info = {
            'token': token,
            'username': username,
        }

        self._login()

    def _get_auth_url(self):
        api_furl = furl('https://accounts.spotify.com/authorize')
        api_furl.args['client_id'] = SPOTIFY_CLIENT_ID
        api_furl.args['redirect_uri'] = 'http://example.com/callback/'
        api_furl.args['scope'] = 'playlist-modify-public'
        api_furl.args['response_type'] = 'token'

        return api_furl.url

    def _login(self):
        self.spotify_api = spotipy.Spotify(auth=self.user_info['token'])
