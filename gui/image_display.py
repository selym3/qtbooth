from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

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


class ImageDisplay(QLabel):

    def __init__(self, imageSupplier):
        super().__init__()

        self.imageSupplier = imageSupplier
        
        self.setAlignment(Qt.AlignCenter)

        # do one update on initialize
        self.update()
        # self.usedPixmap = False

    def update(self):
        image = self.imageSupplier.getImage()

        # if not self.usedPixmap:
            # self.setPixmap(QPixmap.fromImage())
        self.setPixmap(QPixmap.fromImage(image))

