import json
import logging
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import tomllib

scope = 'playlist-read-private,user-library-read'

with open(".env.toml", mode="rb") as fp:
    config = tomllib.load(fp)

if not os.path.isdir(config['log']['path']):
    os.makedirs(config['log']['path'])

logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()
rootLogger.setLevel(logging.INFO)

fileHandler = logging.FileHandler("{0}/{1}.log".format(config['log']['path'], config['log']['filename']))
fileHandler.setLevel(logging.INFO)
fileHandler.setFormatter(logFormatter)
rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)

# authenticate spotify account
def authenticate(username, password):
    pass

# grab all playlist data
def get_playlist_data(playlist_id):
    pass

def get_all_saved_tracks(sp: spotipy.Spotify, limit=50):
    tracks = []
    offset = 0

    rootLogger.info('grabbing tracks: limit={0} offset={1}', limit, offset)
    current = sp.current_user_saved_tracks(limit, offset)['items']
    while current:
        tracks.extend(current)
        offset += limit
        rootLogger.info('grabbing tracks: limit={0} offset={1}', limit, offset)
        current = sp.current_user_saved_tracks(limit, offset)['items']

    return tracks
def main():
    rootLogger.info('starting Spotify Extraction')
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=config['api']['client_id'],
        client_secret=config['api']['client_secret'],
        redirect_uri=config['api']['redirect_uri'],
        scope=scope))

    # setting up files
    if not os.path.isdir('output'):
        os.makedirs('output')

    rootLogger.info('Getting all saved tracks')
    saved_tracks = get_all_saved_tracks(sp)

    rootLogger.info('saving tracks to file')
    with open('output/saved_tracks.json', 'w') as f:
        json.dump(saved_tracks, f, indent=4)

    rootLogger.info('Spotify Extraction complete')

if __name__ == '__main__':
    main()
