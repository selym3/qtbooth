import threading
import time

class DisplayThread(threading.Thread):
    
    def __init__(self, display, hz=50, paused=True):
        threading.Thread.__init__(self)
        self.display = display
        self.wait = 1.0 / hz

        self.paused = paused

        self.running = True
        # self.running = False

    def run(self):
        while self.running:

            if not self.paused:
                self.display.update()
            
            time.sleep(self.wait)
