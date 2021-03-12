from PIL import Image
import numpy as np
import cv2
from PyQt5.QtGui import QImage

class ImageSupplier:
    
    def __init__(self, pathToImage, size=None):
        self.image = Image.open(pathToImage).convert('RGBA')
        self.buffer = np.array(self.image)

        if not size is None:
            self.buffer = cv2.resize(self.buffer, size)

        self.height, self.width, self.channels = self.buffer.shape 

    def getFormat(self):
        imageFormat = None
        
        if self.channels == 3:
            imageFormat = QImage.Format_RGB888
        elif self.channels == 4:
            imageFormat = QImage.Format_RGBA8888

        return imageFormat

    def getImage(self):
        imageFormat = self.getFormat()

        if imageFormat is None:
            return None, None

        return self.buffer, imageFormat