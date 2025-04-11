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
        voice('What do you want to listen to?', 34)
        user_query = input('What song would you like to hear? ').strip()

        if check_exit(user_query):
            continue

        sp = authenticate()
        track = search_song(sp, user_query)

        voice(f'You requested {user_query}', 34)

        if track:
            song = track["name"]
            artist = track["artists"][0]["name"]
            voice(f'Playing {song} by {artist}', 34)
            play_song(sp, track['uri'])
            return