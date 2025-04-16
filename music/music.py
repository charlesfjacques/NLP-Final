from pyttsx3_voice import voice
from music.spotify_utils import authenticate, search_song, play_song
from music.validification import check_title, check_artist, get_song_name_artist

def check_exit(string):
    if 'EXIT' in string.upper():
        voice('Returning to home', 34)
        return True
    return False

def process_music_request():
    print('Processing music request')

    while True:
        voice('What would you like to do?   Play a song or stop? use PLAY.. BY... and STOP...'   , 34)
        user_query = input('Query? ').strip()

        if check_exit(user_query):
            return

        user_song_name, user_song_artist = get_song_name_artist(user_query)
        if not user_song_name:
            voice('I couldn’t find that song. Try again.', 34)
            continue

        sp = authenticate()
        track = search_song(sp, user_song_name)
        if not track:
            voice('No match found on Spotify.', 34)
            continue

        spotify_song_name = track["name"]
        spotify_artists = [artist["name"] for artist in track["artists"]]

        if not check_title(user_song_name, spotify_song_name):
            voice('Song title didn’t match closely enough. Try again.', 34)
            continue

        if user_song_artist:
            if not check_artist(user_song_artist, spotify_artists):
                voice('Artist didn’t match. Try again.', 34)
                continue

        voice(f'Playing {spotify_song_name} by {spotify_artists[0]}', 34)
        play_song(sp, track['uri'])
        
