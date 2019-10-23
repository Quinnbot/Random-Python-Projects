import os
import sys
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

username = sys.argv[1]
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

try:
    token = util.prompt_for_user_token(username)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache={username}")
    token = util.prompt_for_user_token("quinnbot-us")



sp = spotipy.Spotify(auth=token)
