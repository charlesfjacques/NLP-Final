from bs4 import BeautifulSoup
import requests
import pyttsx3
from pyttsx3_voice import voice
import webbrowser
import subprocess
from sports.player import player
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import datetime
import http.client

current_time = datetime.datetime.now()

api_key = '6e738d01052c9576c2fe3d5fb0f30eaf'

def get_date():
    day = 0
    month = 0
    if len(str(current_time.month)) < 2:
        month = '0' + str(current_time.month)
    else:
        month = str(current_time.month)
    if len(str(current_time.day)) < 2:
        day = '0' + str(current_time.day)
    else:
        day = str(current_time.day)
    
    return f'{current_time.year}-{month}-{day}'

def get_info_bsb(team, date=get_date()):

    url = f'https://v1.baseball.api-sports.io/games?date={date}'

    payload={}
    headers = {
    'x-rapidapi-key': '6e738d01052c9576c2fe3d5fb0f30eaf',
    'x-rapidapi-host': 'v1.baseball.api-sports.io'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()
    i_list = []
    for i in range(len(data['response'])):
        if data['response'][i]['league']['name'] != 'MLB':
            i_list.append(i)
    i_list.reverse()
    for i in range(len(i_list)):
        del data['response'][i_list[i]]

    for i in range(len(data['response'])):
        if data['response'][i]['teams']['home']['name'] == team or data['response'][i]['teams']['away']['name'] == team and data['response'][i]['status']['long'] != 'Not Started':
            home = data['response'][i]['teams']['home']['name']
            home_scr = str(data['response'][i]['scores']['home']['total'])
            away = data['response'][i]['teams']['away']['name']
            away_scr = str(data['response'][i]['scores']['away']['total'])

            return f'The {home} played the {away}. The {home} scored {home_scr} runs, and the {away} scored {away_scr} runs.'
        elif data['response'][i]['status']['long'] == 'Not Started':
            return 'The game has not started yet.'
        else:
            return 'Try a different team.'


def get_info_bkb(team, date=get_date()):
    url = f'https://v1.basketball.api-sports.io/games?date={date}'
    url2 = f'https://v1.basketball.api-sports.io/games?date=2025-05-05'

    payload={}
    headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': 'v1.basketball.api-sports.io'
    }

    response = requests.request("GET", url2, headers=headers, data=payload)
    data = response.json()

    i_list = []
    for i in range(len(data['response'])):
        if data['response'][i]['league']['name'] != 'NBA':
            i_list.append(i)
    i_list.reverse()
    for i in range(len(i_list)):
        del data['response'][i_list[i]]

    for i in range(len(data['response'])):
        if data['response'][i]['teams']['home']['name'] == team or data['response'][i]['teams']['away']['name'] == team and data['response'][i]['status']['long'] != 'Not Started':
            home = data['response'][i]['teams']['home']['name']
            home_scr = str(data['response'][i]['scores']['home']['total'])
            away = data['response'][i]['teams']['away']['name']
            away_scr = str(data['response'][i]['scores']['away']['total'])

            return f'The {home} played the {away}. The {home} scored {home_scr} points, and the {away} scored {away_scr} points.'
        elif data['response'][i]['status']['long'] == 'Not Started':
            return ('Game has not started yet')
        else:
            return ('Try a different team')


def get_info_scr(team, date=get_date()):
    url = f'https://v3.football.api-sports.io/fixtures?date={date}'

    payload={}
    headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': 'v3.football.api-sports.io'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    
    for i in range(len(data['response'])):
        if data['response'][i]['teams']['home']['name'] == team or data['response'][i]['teams']['away']['name'] == team and data['response'][i]['status']['long'] != 'Not Started':
            home = data['response'][i]['teams']['home']['name']
            home_scr = str(data['response'][i]['scores']['home']['total'])
            away = data['response'][i]['teams']['away']['name']
            away_scr = str(data['response'][i]['scores']['away']['total'])

            return f'The {home} played the {away}. The {home} scored {home_scr} goals, and the {away} scored {away_scr} goals.'
        elif data['response'][i]['status']['long'] == 'Not Started':
            return (('game', 'not'), ('started', 'yet'))
        else:
            return (('try','a'),('different','team'))




def check_exit(string):
     if 'EXIT' in string.upper():
        voice('Returning to home', 34)
        return True
     return False

def sport_spliter(sport_name):

     sports = ['BASKETBALL','SOCCER','BASEBALL','EXIT']
     voice('Select a sport, state an athletes name, or say exit to return to home',34)

     if sport_name in sports:
          if sport_name == 'BASKETBALL':
               sport_team = input('which team: ').lower()
               sport_team = sport_team.capitalize()
               voice(get_info_bkb(sport_team))
          elif sport_name == 'SOCCER':
               sport_team = input('which team: ').lower()
               sport_team = sport_team.capitalize()
               voice(get_info_scr())
          elif sport_name == 'BASEBALL':
               sport_team = input('which team: ').lower()
               sport_team = sport_team.capitalize()
               voice(get_info_bsb(sport_team))
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
               voice('state the sport you would like to investigate',34)
               sport_name = input('state sport: ').upper()
               sport_spliter(sport_name)
               
          else:
               voice('sorry could not process your request',34)
               exit