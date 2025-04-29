from bs4 import BeautifulSoup
import requests
from pyttsx3_voice import voice
import webbrowser
import subprocess


def player(name):
     if ' ' in name:
          first_last = name.replace(' ','_')
     else:
          first_last = name

     letter_list = []
 
     for letters in name:
          letter_list.append(letters)
 
     checker = letter_list[0]
     # print(checker)
 
     print(f"Formatted name for URL: {first_last}")
 
     search_term = f'{input}'
 
     url = "https://www.google.com.tr//search?q={}".format(search_term)
 
     # webbrowser.open(url)
 
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