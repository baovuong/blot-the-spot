import spotipy
from spotipy.oauth2 import SpotifyOAuth
import tomllib

# authenticate spotify account
def authenticate(username, password):
    pass

# grab all playlist data
def get_playlist_data(playlist_id):
    pass

def main():
    with open("app.toml", mode="rb") as fp:
        config = tomllib.load(fp)

    scope = "user-library-read"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=config['spotify_app']['client_id'],
        client_secret=config['spotify_app']['client_secret'],
        redirect_uri=config['spotify_app']['redirect_uri'],
        scope=scope))

    results = sp.current_user_saved_tracks()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])


if __name__ == '__main__':
    main()
