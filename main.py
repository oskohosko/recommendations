import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Test
playlist_uri = "spotify:Oskar_Hosken:PROVINCIAL:playlist:07o6kTp4nYhgcbIvVQpcEq"
username, playlist_id, playlist_name = playlist_uri.split(':')[1], playlist_uri.split(':')[4], playlist_uri.split(':')[2]
sp_tracks = sp.user_playlist(username, playlist_id, 'tracks')
playlist_df = pd.DataFrame(columns=sp_tracks['tracks']['items'][0]['track'].keys())

# populating dataframe
for track in sp_tracks['tracks']['items']:
    playlist_df.loc[len(playlist_df)] = track['track']
