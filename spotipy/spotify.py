#import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify()
cid ="38e5f6f519064694950f556f6226afff"
secret = "6d6e32bfe7bd4bb6976c06292622f8e0"
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False
#playlist = sp.user_playlist("DREAMERS and others", "4ECUgPO2v26M9JeOo2aWcT")
playlist = sp.user_playlist("2019", "7EC7Nw0YPaX8QvAwnXPr2S")
songs = playlist["tracks"]["items"]
ids = []
devices = sp.devices()
for i in range(len(songs)):
    ids.append(songs[i]["track"]["id"])
    #print(songs[i])
    print(songs[i]["track"]["name"] + "\n  id:  "+ songs[i]["track"]["id"] + "\n")
