from bs4 import BeautifulSoup
import requests
from voice.pyttsx3_voice import voice
import webbrowser
import subprocess
from sports.player import player
import math
import datetime
import http.client
import string

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

def get_yest():
    day = 0
    month = 0
    if len(str(current_time.month)) < 2:
        month = '0' + str(current_time.month)
    else:
        month = str(current_time.month)
    if len(str(current_time.day - 1)) < 2:
        day = '0' + str(current_time.day - 1)
    else:
        day = str(current_time.day - 1)
    
    return f'{current_time.year}-{month}-{day}'


def get_info_bsb(team, date=get_date(), yest=get_yest()):

    url = f'https://v1.baseball.api-sports.io/games?date={date}'
    url_yest = f'https://v1.baseball.api-sports.io/games?date={yest}'

    payload={}
    headers = {
    'x-rapidapi-key': '6e738d01052c9576c2fe3d5fb0f30eaf',
    'x-rapidapi-host': 'v1.baseball.api-sports.io'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_yest = requests.request("GET", url_yest, headers=headers, data=payload)

    data = response.json()
    i_list = []
    data_yest = response_yest.json()
    i_list_yest = []
    for i in range(len(data['response'])):
        if data['response'][i]['league']['name'] != 'MLB':
            i_list.append(i)
    i_list.reverse()
    for i in range(len(i_list)):
        del data['response'][i_list[i]]


    for i in range(len(data_yest['response'])):
        if data_yest['response'][i]['league']['name'] != 'MLB':
            i_list_yest.append(i)
    i_list_yest.reverse()
    for i in range(len(i_list_yest)):
        del data_yest['response'][i_list_yest[i]]


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
            for i in range(len(data_yest['response'])):
                if data_yest['response'][i]['teams']['home']['name'] == team or data_yest['response'][i]['teams']['away']['name'] == team and data_yest['response'][i]['status']['long'] != 'Not Started':
                    home = data_yest['response'][i]['teams']['home']['name']
                    home_scr = str(data_yest['response'][i]['scores']['home']['total'])
                    away = data_yest['response'][i]['teams']['away']['name']
                    away_scr = str(data_yest['response'][i]['scores']['away']['total'])

                    return f'The {home} played the {away}. The {home} scored {home_scr} runs, and the {away} scored {away_scr} runs.'
                elif data_yest['response'][i]['status']['long'] == 'Not Started':
                    return 'The game has not started yet.'
                else:
                    'Try a different team'
        


def get_info_bkb(team, date=get_date(), yest=get_yest()):
    url = f'https://v1.basketball.api-sports.io/games?date={date}'
    url_yest = f'https://v1.basketball.api-sports.io/games?date={yest}'

    payload={}
    headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': 'v1.basketball.api-sports.io'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_yest = requests.request("GET", url_yest, headers=headers, data=payload)

    data = response.json()
    i_list = []
    data_yest = response_yest.json()
    i_list_yest = []
    for i in range(len(data['response'])):
        if data['response'][i]['league']['name'] != 'NBA':
            i_list.append(i)
    i_list.reverse()
    for i in range(len(i_list)):
        del data['response'][i_list[i]]

    for i in range(len(data_yest['response'])):
        if data_yest['response'][i]['league']['name'] != 'NBA':
            i_list_yest.append(i)
    i_list_yest.reverse()
    for i in range(len(i_list_yest)):
        del data_yest['response'][i_list_yest[i]]

    for i in range(len(data['response'])):
        if data['response'][i]['teams']['home']['name'] == team or data['response'][i]['teams']['away']['name'] == team and data['response'][i]['status']['long'] != 'Not Started':
            home = data['response'][i]['teams']['home']['name']
            home_scr = str(data['response'][i]['scores']['home']['total'])
            away = data['response'][i]['teams']['away']['name']
            away_scr = str(data['response'][i]['scores']['away']['total'])

            return f'The {home} played the {away}. The {home} scored {home_scr} points, and the {away} scored {away_scr} points.'
        elif data['response'][i]['status']['long'] == 'Not Started':
            return 'Game has not started yet'
        else:
            for i in range(len(data_yest['response'])):
                if data_yest['response'][i]['teams']['home']['name'] == team or data_yest['response'][i]['teams']['away']['name'] == team and data_yest['response'][i]['status']['long'] != 'Not Started':
                    home = data_yest['response'][i]['teams']['home']['name']
                    home_scr = str(data_yest['response'][i]['scores']['home']['total'])
                    away = data_yest['response'][i]['teams']['away']['name']
                    away_scr = str(data_yest['response'][i]['scores']['away']['total'])

                    return f'The {home} played the {away}. The {home} scored {home_scr} points, and the {away} scored {away_scr} points.'
                elif data_yest['response'][i]['status']['long'] == 'Not Started':
                    return 'The game has not started yet.'
                else:
                    'Try a different team'


def get_info_scr(team, date=get_date(), yest=get_yest()):
    url = f'https://v3.football.api-sports.io/fixtures?date={date}'
    url_yest = f'https://v3.football.api-sports.io/fixtures?date={yest}'

    payload={}
    headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': 'v3.football.api-sports.io'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_yest = requests.request("GET", url_yest, headers=headers, data=payload)

    data = response.json()
    data_yest = response_yest.json()
    
    for i in range(len(data['response'])):
        if data['response'][i]['teams']['home']['name'] == team or data['response'][i]['teams']['away']['name'] == team and data['response'][i]['status']['long'] != 'Not Started':
            home = data['response'][i]['teams']['home']['name']
            home_scr = str(data['response'][i]['scores']['home']['total'])
            away = data['response'][i]['teams']['away']['name']
            away_scr = str(data['response'][i]['scores']['away']['total'])

            return f'The {home} played the {away}. The {home} scored {home_scr} goals, and the {away} scored {away_scr} goals.'
        elif data['response'][i]['status']['long'] == 'Not Started':
            return 'Game has not started yet.'
        else:
            for i in range(len(data_yest['response'])):
                if data_yest['response'][i]['teams']['home']['name'] == team or data_yest['response'][i]['teams']['away']['name'] == team and data_yest['response'][i]['status']['long'] != 'Not Started':
                    home = data_yest['response'][i]['teams']['home']['name']
                    home_scr = str(data_yest['response'][i]['scores']['home']['total'])
                    away = data_yest['response'][i]['teams']['away']['name']
                    away_scr = str(data_yest['response'][i]['scores']['away']['total'])

                    return f'The {home} played the {away}. The {home} scored {home_scr} points, and the {away} scored {away_scr} points.'
                elif data_yest['response'][i]['status']['long'] == 'Not Started':
                    return 'The game has not started yet.'
                else:
                    'Try a different team'
            


def sport_api():
     return 

def check_exit(string):
     if 'EXIT' in string.upper():
        voice('Returning to home', 34)
        return True
     return False

def sport_spliter(sport_name):

     sports = ['BASKETBALL','SOCCER','BASEBALL','EXIT']
     voice('State the full team name, or say exit to return to home',34)

     if sport_name in sports:
          if sport_name == 'BASKETBALL':
               sport_team = input('which team: ').lower()
               sport_team = string.capwords(sport_team)
               voice(get_info_bkb(sport_team))
          elif sport_name == 'SOCCER':
               sport_team = input('which team: ').lower()
               sport_team = string.capwords(sport_team)
               voice(get_info_scr(sport_team))
          elif sport_name == 'BASEBALL':
               sport_team = input('which team: ').lower()
               sport_team = string.capwords(sport_team)
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
               voice('state the sport you would like to investigate, basketball, baseball, or soccer',34)
               sport_name = input('state sport: ').upper()
               sport_spliter(sport_name)
               
          else:
               voice('sorry could not process your request',34)
               exit