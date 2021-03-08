import numpy as np
from PyQt5.QtGui import QImage

class ColorSupplier:
    
    def __init__(self, color, width, height):
        self.color = color
        self.buffer = np.full((width, height, 3), color, dtype=np.uint8)

        self.width, self.height = width, height
        self.image = None

    def getImage(self):
        if self.image == None:
            self.image = QImage(self.buffer, self.width, self.height, QImage.Format_RGB888)

        return self.image