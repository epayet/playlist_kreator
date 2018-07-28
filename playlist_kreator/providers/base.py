class BaseProvider:
    def __init__(self):
        self.user_info = {}

    def create_playlist_from_top_songs(self, playlist_name, artists, max_top_tracks=2):
        print()
        song_ids = []

        for artist_name in artists:
            artist_id = self.get_artist_id(artist_name)

            if not artist_id:
                print('{}: Not Found. Skipping'.format(artist_name))
                continue

            artist_top_song_ids = self.get_artist_top_song_ids(artist_id, max_top_tracks)

            if len(artist_top_song_ids) == 0:
                print('{}: Exists but no songs found. Skipping'.format(artist_name))
                continue

            song_ids = song_ids + artist_top_song_ids
            print('{}: Found {} song(s). Will add'.format(artist_name, len(artist_top_song_ids)))

        playlist_id = self.create_playlist(playlist_name)
        print('\nCreated playlist "{}" ({})'.format(playlist_name, playlist_id))

        self.add_songs_to_playlist(playlist_id, song_ids)
        print('Added {} songs to the playlist'.format(len(song_ids)))
        print('All done. Enjoy! 🤘')

    def get_artist_id(self, artist_name):
        pass

    def get_artist_top_song_ids(self, artist_id, max_top_tracks):
        return []

    def create_playlist(self, playlist_name):
        pass

    def add_songs_to_playlist(self, playlist_id, song_ids):
        pass

    def get_user_info(self, args):
        pass
