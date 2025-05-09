import threading
import subprocess
import time

class TTSEngine(threading.Thread):
        def __init__(self):
                super().__init__()
                self.running = False
                self.to_speak = []
                self.process = None
        def run(self):
                self.running = True
                while self.running:
                        if len(self.to_speak) > 0:
                                phrases = self.to_speak
                                self.to_speak = []
                                self.process = subprocess.Popen(["python3", "speak_subprocess.py", *phrases])
                                self.process.wait()
                                self.process = None
                        time.sleep(0.1)
        def say(self, text):
                self.to_speak.append(text)
        def interrupt(self):
                self.to_speak = []
                if self.process is not None:
                        self.process.terminate()
                        self.process = None
        def exit(self):
                self.running = False

VOICE = "com.apple.eloquence.en-US.Eddy"