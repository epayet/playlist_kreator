from getpass import getpass
from gmusicapi import Mobileclient

from playlist_kreator.providers.base import BaseProvider


class GMusicProvider(BaseProvider):
    def get_artist_id(self, artist_name):
        search = self.gmusic_api.search(artist_name)

        if len(search["artist_hits"]) == 0:
            return None

        return search["artist_hits"][0]["artist"]["artistId"]

    def get_artist_top_song_ids(self, artist_id, max_top_tracks):
        artist = self.gmusic_api.get_artist_info(artist_id, include_albums=False,
                                                 max_top_tracks=max_top_tracks, max_rel_artist=0)

        if 'topTracks' not in artist:
            return []

        return [track['nid'] for track in artist['topTracks']]

    def create_playlist(self, playlist_name):
        # TODO add nice description
        return self.gmusic_api.create_playlist(playlist_name)

    def add_songs_to_playlist(self, playlist_id, song_ids):
        self.gmusic_api.add_songs_to_playlist(playlist_id, song_ids)

    def get_user_info(self, args):
        print("It will need an email and an application password for Google Music")
        print("You can set it up here: https://myaccount.google.com/apppasswords\n")

        email = args.username
        if email:
            print("Email: {}".format(email))
        else:
            email = input("Email:")

        password = getpass("Password:")

        self._login(email, password)

    def _login(self, email, password):
        self.gmusic_api = Mobileclient()
        logged_in = self.gmusic_api.login(email, password, Mobileclient.FROM_MAC_ADDRESS)

        if not logged_in:
            raise Exception('Could not connect')
