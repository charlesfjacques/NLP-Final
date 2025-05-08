from pyttsx3_voice import voice, end_voice, interrupt_voice
from sports.sports import process_sports_request
from weather.weather import process_weather_request
from music.music import process_music_request
from speech_to_text.listen import listen, load, check_for_word

exit_key_words = ['STOP', 'EXIT', 'LEAVE']
weather_key_words = ['WEATHER', 'WHETHER']
music_key_words = ['MUSIC', 'SONG', 'LISTEN']
sports_key_words = ['SPORTS', 'PLAYERS']

#
#  This is the main driver program for the "Alexa" Project 
#

def main():

    print("Initializing text to speech")
    load()

    voice("Welcome to Alehxa",34)
    voice('Please select one of the following categories for your question',34)
    voice("Weather, Music, Sports. Say exit to exit", 34)

    user_query = listen()
    interrupt_voice()    
    print(user_query)
    
    if check_for_word(user_query, exit_key_words):
        return
    
    elif check_for_word(user_query, weather_key_words):
        process_weather_request()

    elif check_for_word(user_query, music_key_words):
        process_music_request()

    elif check_for_word(user_query, sports_key_words):
        process_sports_request()
    

main()
end_voice()