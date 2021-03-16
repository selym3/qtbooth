import numpy as np
from PyQt5.QtGui import QImage

from .image_format import RGB_8

class ColorSupplier:
    
    def __init__(self, color, width, height):
        self.buffer = np.full((height, width, 3), color, dtype=np.uint8)

    def getImage(self):
        return self.buffer, RGB_8 # QImage.Format_RGB888