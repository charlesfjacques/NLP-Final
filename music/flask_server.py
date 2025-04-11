from flask import Flask, request, redirect
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

app = Flask(__name__)

sp_oauth = SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri="http://localhost:8080/callback",
    scope="user-read-playback-state user-modify-playback-state",
    cache_path=".cache"  
)

@app.route("/callback")
def callback():
    code = request.args.get('code')
    if not code:
        return "Error: No authorization code received.", 400

    token_info = sp_oauth.get_access_token(code)
    access_token = token_info['access_token']
    print("Access Token: ", access_token)

    return redirect("http://localhost:8080/success")

@app.route("/success")
def success():
    return "Authorization successful! You can now use the app."

if __name__ == "__main__":
    app.run(port=8080)
