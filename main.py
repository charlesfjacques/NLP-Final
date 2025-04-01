from bs4 import BeautifulSoup
import requests
import pyttsx3
import webbrowser
import subprocess
import voice


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

input = 'eliud kipchoge'

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
        i = 0
        webpage_text = soup.find_all('p')[i].get_text()

        if webpage_text[0] != checker:
                webpage_text = soup.find_all('p')[i+1].get_text()

        print(webpage_text[0:1000])
        speech = webpage_text[0:100]
except:
       speech = "Player not found"

voice(speech,34)

