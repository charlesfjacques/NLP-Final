import sounddevice as sd
import queue
import json
from vosk import Model, KaldiRecognizer

#SETTINGS

settings_sample_rate = 16000
settings_block_size = 8000
settings_model = "speech_to_text/vosk_stt/current_model"

model = Model(settings_model)
rec = KaldiRecognizer(model, 16000)
q = queue.Queue()

def check_microphone():
    devices = sd.query_devices()
    input_devices = [d for d in devices if d['max_input_channels'] > 0]
    if not input_devices:
        print("No microphone found.")
        return False
    print("Microphones found:")
    for i, d in enumerate(input_devices):
        print(f"{i}: {d['name']}")
    return True

def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

def vosk_listen():
    if check_microphone() == False:
        print("No mic")
        return input()
    with sd.RawInputStream(samplerate=settings_sample_rate, blocksize=settings_block_size, dtype='int16',
                        channels=1, callback=callback):
        
        print("Listening...") 

        keep_listening = True

        while keep_listening:
            data = q.get()
            if rec.AcceptWaveform(data):

                result = json.loads(rec.Result())
                current_text = result.get("text", "")

                if current_text.strip() != "":
                    return current_text
                    
                print("You said:", current_text)

