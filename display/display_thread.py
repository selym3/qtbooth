import threading
import time

class DisplayThread(threading.Thread):
    
    def __init__(self, display, hz=50, paused=True):
        threading.Thread.__init__(self)

        self.display = display

        self.wait = 1.0 / hz
        self.paused = paused

        self.running = True

        # fil this in once on initialization
        # np array, QImage format
        self.frame = self.display.supplier.getImage()

    def run(self):
        while self.running:

            if not self.paused:
                # If you are not paused, get another frame from the supplier
                self.frame = self.display.supplier.getImage()

            filtered = self.frame[0]

            # Filter and display the available frame
            if not self.display.filter is None:
                filtered = self.display.filter.filter(filtered)
            
            self.display.update(filtered, self.frame[1])

            time.sleep(self.wait)
