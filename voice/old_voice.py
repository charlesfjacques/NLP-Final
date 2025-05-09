import pyttsx3

engine = pyttsx3.init()
VOICE = "com.apple.eloquence.en-US.Eddy"
# the voice_id argument is ignored
def old_voice(text, voice_id = 99):
        voices = engine.getProperty('voices')
        # print([v.id for v in voices])
        engine.setProperty('voice', VOICE)
        engine.setProperty('rate', 170)
        # default female id is 34
        # default male id is 19

        engine.say(text)
        engine.runAndWait()

        engine.save_to_file(text, 'output.wav')
        engine.runAndWait()
        return