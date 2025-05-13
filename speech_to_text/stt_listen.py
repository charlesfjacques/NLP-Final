import speech_to_text.vosk_stt.vosk_stt as vsk
def listen():
    return vsk.vosk_listen()
def load():
    vsk.load()
