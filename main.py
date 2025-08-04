import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import tomllib

# authenticate spotify account
def authenticate(username, password):
    pass

# grab all playlist data
def get_playlist_data(playlist_id):
    pass

def get_all_saved_tracks(sp: spotipy.Spotify, limit=50):
    tracks = []
    offset = 0

    current = sp.current_user_saved_tracks(limit, offset)['items']
    while current:
        tracks.extend(current)
        offset += limit
        current = sp.current_user_saved_tracks(limit, offset)['items']

    return tracks
def main():
    with open("app.toml", mode="rb") as fp:
        config = tomllib.load(fp)

    scope = 'playlist-read-private,user-library-read'

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=config['spotify_app']['client_id'],
        client_secret=config['spotify_app']['client_secret'],
        redirect_uri=config['spotify_app']['redirect_uri'],
        scope=scope))

    saved_tracks = get_all_saved_tracks(sp)
    print(len(saved_tracks))


    with open('saved_tracks.json', 'w') as f:
        json.dump(saved_tracks, f)


if __name__ == '__main__':
    main()
