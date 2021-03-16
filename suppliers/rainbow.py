import colorsys
import numpy as np
import math

from PyQt5.QtGui import QImage

from .image_format import RGB_8

class RainbowSupplier:
    
    def __init__(self, speed, width, height):
        self.width, self.height = width, height
        
        self.speed = speed

        self.updates = 0
        self.h = 0
        self.s, self.v = 1, 1

    def getColor(self):
        self.updates += self.speed

        self.h = (math.sin(self.updates) + 1) / 2.0

        # between [0,1]
        rgb = colorsys.hsv_to_rgb(self.h, self.s, self.v)

        return tuple(int(round(i * 255)) for i in rgb)

    def getImageArray(self):
        return np.full((self.height, self.width, 3), self.getColor(), dtype=np.uint8)

    def getImage(self):
        return self.getImageArray(), RGB_8 # QImage.Format_RGB888
