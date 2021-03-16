from PIL import Image
import numpy as np
import cv2
from PyQt5.QtGui import QImage

from .image_format import RGB_8, RGBA_8

class ImageSupplier:
    
    def __init__(self, pathToImage, size=None):
        self.image = Image.open(pathToImage).convert('RGB')
        self.buffer = np.array(self.image)

        if not size is None:
            self.buffer = cv2.resize(self.buffer, size)

        self.height, self.width, self.channels = self.buffer.shape 

    def getFormat(self):
        imageFormat = None
        
        if self.channels == 3:
            imageFormat = RGB_8 #  QImage.Format_RGB888
        elif self.channels == 4:
            # imageFormat = RGBA_8 # QImage.Format_RGBA8888
            pass

        return imageFormat

    def getImage(self):
        imageFormat = self.getFormat()

        if imageFormat is None:
            return None, None

        return self.buffer, imageFormat