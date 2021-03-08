from PIL import Image
import numpy as np
from PyQt5.QtGui import QImage

class ImageSupplier:
    
    def __init__(self, pathToImage):
        self.image = Image.open(pathToImage).convert('RGBA')
        self.buffer = np.array(self.image)
        self.height, self.width, self.channels = self.buffer.shape 

        # try:
        #     self.image = Image.open(pathToImage)
        #     self.buffer = np.array(self.image)
        #     self.height, self.width, self.channels = self.buffer.shape 
        # except Exception as e:
        #     # This is really dumb , but if it doesnt have a channel, it 
        #     # is probably a png with an -A channel that needs to be reloaded
        #     self.image = self.image.convert('RGBA')
        #     self.buffer = np.array(self.image)
        #     self.height, self.width, self.channels = self.buffer.shape 

        self.qImage = None

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
            return None

        if self.qImage is None:
            self.qImage = QImage(self.buffer, self.width, self.height, imageFormat) 

        return self.qImage