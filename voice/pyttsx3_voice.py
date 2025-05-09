from voice.TTSEngine import TTSEngine
from config import skip_speak
from voice.old_voice import old_voice
engine = TTSEngine()
engine.start()
# the voice_id argument is ignored
def voice(text, voice_id = 99):
        if skip_speak:
                print(text)
                engine.say(text)
        else:
                old_voice(text)
                

def interrupt_voice():
        engine.interrupt()

def end_voice():
        engine.exit()