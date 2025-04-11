from bs4 import BeautifulSoup
import requests
from pyttsx3_voice import voice
import webbrowser
import subprocess

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

    name = input("Enter player name: ")
    print(name)

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

