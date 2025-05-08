import sys
import pyttsx3
from TTSEngine import VOICE

def init_engine():
    engine = pyttsx3.init()
    engine.setProperty('voice', VOICE)
    engine.setProperty('rate', 170)
    return engine

def say(s):
    engine.say(s)
    engine.runAndWait()

engine = init_engine()
for phrase in sys.argv[1:]:
    say(str(phrase))