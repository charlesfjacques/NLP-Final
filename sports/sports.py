from bs4 import BeautifulSoup
import requests
from pyttsx3_voice import voice
import webbrowser
import subprocess
from sports.player import player

def sport_api():
     return 

def check_exit(string):
     if 'EXIT' in string.upper():
        voice('Returning to home', 34)
        return True
     return False

def sport_spliter(sport_name):

     sports = ['BASKETBALL','FOOTBALL','SOCCER','BASEBALL','EXIT']
     voice('Select a sport, state an athletes name, or say exit to return to home',34)

     if sport_name in sports:
          if sport_name == 'BASKETBALL':
               print('basketball')
          elif sport_name == 'FOOTBALL':
               print('football')
          elif sport_name == 'SOCCER':
               print('soccer')
          elif sport_name == 'BASEBALL':
               print('baseball')
          elif sport_name == 'EXIT':
               voice('Returning to home',34)
     else:
          voice('Sorry, unable to proccess that sport. Try another sport or say exit to return to home',34)
          exit


def process_sports_request() :
     print('processing sports request')

      
     while True:
          voice('If you would like to learn about an atlhete say athlete, if you would like to learn about a sport say sport, if you would like to exit say exit',34)
          answer = input('Choice:' ).upper()

          if check_exit(answer):
               return
          
          if answer == 'ATHLETE':
               voice("state the name of the athlete",34)
               name = input('athlete name: ')
               print(name)
               player(name)

          elif answer == 'SPORT':
               # voice('state the sport you would like to investigate',34)
               # sport_name = input('state sport: ').upper()
               # sport_spliter(sport_name)
               sport_api()
               
          else:
               voice('sorry could not process your request',34)
               exit


