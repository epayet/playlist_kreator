from playlist_kreator.providers.gmusic import GMusicProvider
from playlist_kreator.providers.spotify import SpotifyProvider

PROVIDERS = {
    'gmusic': GMusicProvider(),
    'spotify': SpotifyProvider(),
}


def get_provider(provider_name):
    return PROVIDERS[provider_name]
