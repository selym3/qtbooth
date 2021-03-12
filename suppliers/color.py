import numpy as np
from PyQt5.QtGui import QImage

class ColorSupplier:
    
    def __init__(self, color, width, height):
        self.color = color
        self.buffer = np.full((width, height, 3), color, dtype=np.uint8)

        self.width, self.height = width, height

    def getImage(self):
        return self.buffer, QImage.Format_RGB888