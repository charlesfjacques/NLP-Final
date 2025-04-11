import pyttsx3

def voice(text,voice_id = 34):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[voice_id].id)
        
        # default female id is 34
        # default male id is 19

        engine.say(text)
        engine.runAndWait()

        engine.save_to_file(text, 'output.wav')
        engine.runAndWait()
        return

