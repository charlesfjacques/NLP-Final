from bs4 import BeautifulSoup
import requests
import pyttsx3
import webbrowser
import subprocess
import voice


name = input("Enter player name: ")
print(name)

def voice(text,voice_id):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[voice_id].id)
        # default female id is 34
        # default male id is 19

        # for voice in voices:
        #         print(f"Voice: {voice.name}, ID: {voice.id}")

        engine.say(text)
        engine.runAndWait()

        engine.save_to_file(text, 'output.wav')
        engine.runAndWait()
        return

def process_weather_request() :
    print('processing weather request')

def process_sports_request() :
    print('processing sports request')
    sports = ['BASKETBALL','FOOTBALL','SOCCER','BASEBALL']
    sport_catagory = ''
    while sport_catagory != 'EXIT':
        voice('Select a sport or say exit to return to home',34)
        sport_catagory = input('What is your choice: ').upper()
        if sport_catagory in sports:
              if sport_catagory == 'BASKETBALL':
                    print('basketball')
              elif sport_catagory == 'FOOTBALL':
                    print('football')
              elif sport_catagory == 'SOCCER':
                    print('soccer')
              elif sport_catagory == 'BASEBALL':
                    print('baseball')
        else:
              voice('Sorry, unable to proccess that sport. Try another sport or say exit to return to home',34)

def process_music_request() :
    print('processing music request')

def process_current_event_request() :
    print('processing current event request')
#
#  This is the main driver program for the "Alexa" Project
#
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
            process_weather_request()
        elif user_category == 'SPORTS' :
            process_sports_request()
        elif user_category == 'MUSIC' :
            process_music_request()
        elif user_category == 'CURRENT EVENTS' :
            process_current_event_request()
        else :
            exit(0)
    else :
        voice('Sorry, your response does not match any of the categories',34)

input = name

if ' ' in input:
                first_last = input.replace(' ','_')
else:
        first_last = input

letter_list = []
for letters in input:
        letter_list.append(letters)

checker = letter_list[0]
print(checker)

print(f"Formatted name for URL: {first_last}")


search_term = f'{input}'
url = "https://www.google.com.tr//search?q={}".format(search_term)
webbrowser.open(url)

link = "https://en.wikipedia.org/wiki/{}".format(first_last)
print(f"Fetching URL: {link}")

r = requests.get(link)
soup = BeautifulSoup(r.text, 'html.parser')

try:
        i = 1
        webpage_text = soup.find_all('p')[i].get_text()

        if webpage_text[0] != checker:
                webpage_text = soup.find_all('p')[i+1].get_text()

        print(webpage_text[0:1000])
        speech = webpage_text[0:100]
except:
       speech = "Player not found"

voice(speech,34)

