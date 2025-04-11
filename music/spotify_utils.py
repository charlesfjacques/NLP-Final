import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
import webbrowser
import subprocess
import time


def authenticate():
    load_dotenv()
    """Authenticate user only if no cached token exists."""
    sp_oauth = SpotifyOAuth(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
        redirect_uri="http://localhost:8080/callback",
        scope="user-read-playback-state user-modify-playback-state",
        cache_path=".cache" 
    )

    token_info = sp_oauth.get_cached_token()
    if token_info:
        print("Using cached token!")
        return spotipy.Spotify(auth_manager=sp_oauth)

    print("No cached token found. Starting authentication...")

    os.system("python flask_server.py &")

    auth_url = sp_oauth.get_authorize_url()
    print("Opening authentication URL:", auth_url)
    os.system(f"python -m webbrowser -t \"{auth_url}\"")

    return spotipy.Spotify(auth_manager=sp_oauth)

def search_song(sp, query):
    results = sp.search(q=query, type="track", limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        return track
    else:
        print("No results found.")
        return None

def play_song(sp, song_uri):

    devices = sp.devices()

    if not devices['devices']:
        print("No active devices found. Opening Spotify...")

        try:
            subprocess.run(["open", "-a", "Spotify"])
        except FileNotFoundError:
            try:
                subprocess.run(["spotify"]) 
            except FileNotFoundError:
                try:
                    subprocess.run(["start", "spotify"], shell=True)
                except FileNotFoundError:
                    webbrowser.open("https://open.spotify.com/")  

        while not devices['devices']:
            devices = sp.devices()
            print("Please open spotify on a device...")
            time.sleep(1)
            
        

    device_id = devices['devices'][0]['id']
    sp.start_playback(device_id=device_id, uris=[song_uri])
    print(f"Playing {song_uri} on {devices['devices'][0]['name']}")

def open_url(url):
    webbrowser.open(url)