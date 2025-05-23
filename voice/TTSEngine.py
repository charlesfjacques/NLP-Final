import threading
import subprocess
import time
import os.path as path

here = path.abspath(__file__)
subprocess_path = path.join(path.dirname(here), "speak_subprocess.py")

INTERRUPT_AFTER = 0.5

class TTSEngine(threading.Thread):
        def __init__(self):
                super().__init__()
                self.running = False
                self.to_speak = []
                self.process = None
                self.last_spoke = 0
        def run(self):
                self.running = True
                while self.running:
                        if len(self.to_speak) > 0:
                                phrases = self.to_speak
                                self.to_speak = []
                                self.process = subprocess.Popen(["python3", subprocess_path, *phrases])
                                self.process.wait()
                                self.process = None
                        time.sleep(0.1)
        def say(self, text):
                now = time.clock_gettime(time.CLOCK_REALTIME)
                if now-self.last_spoke >= INTERRUPT_AFTER:
                        self.interrupt()
                self.last_spoke = now
                self.to_speak.append(str(text))

        def interrupt(self):
                self.to_speak = []
                if self.process is not None:
                        self.process.terminate()
                        self.process = None
        def exit(self):
                self.running = False

VOICE = "com.apple.eloquence.en-US.Eddy"