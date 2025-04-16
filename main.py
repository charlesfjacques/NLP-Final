from pyttsx3_voice import voice
from sports.sports import process_sports_request
# from weather.weather import process_weather_request
# import weather.parser
# from music.music import process_music_request
# from current_events.current_events import process_current_event_request


#
#  This is the main driver program for the "Alexa" Project
#
def main():
    categories = ['WEATHER','SPORTS','MUSIC','CURRENT EVENTS','EXIT']
    user_category = ''
    voice("Welcome to Alexa",34)
    while user_category != 'EXIT' :
        voice('Please select one of the following categories for your question',34)
        voice('\n''WEATHER\nSPORTS\nMUSIC\nCURRENT EVENTS\nEXIT\n',34)
        user_category = input('What is your choice : ').upper()
        #print(user_category)

        if user_category in categories :
            if user_category == 'WEATHER' :
                # process_weather_request()
                continue
            elif user_category == 'SPORTS' :
                process_sports_request()
            elif user_category == 'MUSIC' :
                # process_music_request()
                continue
            elif user_category == 'CURRENT EVENTS' :
                # process_current_event_request()
                continue
            else :
                exit(0)
        else :
            voice('Sorry, your response does not match any of the categories',34)

main()