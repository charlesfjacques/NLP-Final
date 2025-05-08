from TTSEngine import TTSEngine
engine = TTSEngine()
engine.start()
# the voice_id argument is ignored
def voice(text, voice_id = 99):
        print(text)
        engine.say(text)

def interrupt_voice():
        engine.interrupt()

def end_voice():
        engine.exit()