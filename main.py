from pyttsx3_voice import voice
from sports.sports import process_sports_request
from weather.weather import process_weather_request
from music.music import process_music_request
from speech_to_text.speech import listen

#
#  This is the main driver program for the "Alexa" Project
#
def main():
    categories = ['WEATHER','SPORTS','MUSIC']
    user_category = ''
    voice("Welcome to Alehxa",34)
    while user_category != 'EXIT' :
        voice('Please select one of the following categories for your question',34)
        voice(" ".join(categories)+" or exit", 34)
        user_category = listen.upper()
        
        print(user_category)
        
        if user_category == "WHETHER":
            user_category = "WEATHER"

        if user_category == "EXIT":
            exit(0)
            
        if user_category in categories :
            if user_category == 'WEATHER' :
                process_weather_request()
                continue
            elif user_category == 'SPORTS' :
                process_sports_request()
            elif user_category == 'MUSIC' :
                process_music_request()
                continue
        else :
            voice('Sorry, your response does not match any of the categories',34)

main()