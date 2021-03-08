import numpy as np
import math
import colorsys

from PyQt5.QtGui import QImage

from .image_modifiers import BooleanModifier, NumberModifier

from PIL import Image

import cv2

class WebcamSupplier:

    CAMERA_INSTANCE = None

    def __init__(self, width, height):
        self.width, self.height = width, height

        if WebcamSupplier.CAMERA_INSTANCE is None:
            WebcamSupplier.CAMERA_INSTANCE = cv2.VideoCapture(0)

        # reference to singleton camera
        self.webcam = WebcamSupplier.CAMERA_INSTANCE

        self.modifiers = [ 
            BooleanModifier("Inverted", False), 
            NumberModifier("Blur", 1, 10) 
        ] 

    # def getModifiers(self):
    #     # if self.modifiers is None:
    #         # self.modifiers = [ BooleanModifier("Inverted", False) ] 

    #     return self.modifiers
    
    # def clearModifiers(self):
        # self.modifiers = None

    def getImageArray(self):
        ret, frame = self.webcam.read()

        frame = cv2.resize(frame, (self.width, self.height), interpolation=cv2.INTER_LANCZOS4)
 
        if not self.modifiers is None:
            frame = self.applyFilters(frame)

        return frame

    def applyFilters(self, img):
        if self.modifiers[0].isOn():
            img = cv2.flip(img, 1)
        
        blurAmount = int(self.modifiers[1].getValue())
        img = cv2.blur(img, (blurAmount, blurAmount))
        
        return img

    def getImage(self):
        frame = self.getImageArray()

        return QImage(frame, self.width, self.height, QImage.Format_BGR888)

class FlippedWebcamSupplier(WebcamSupplier):

    def __init__(self, width, height, direction=0):
        super().__init__(width, height)
        self.direction = direction

    def getImageArray(self):
        return cv2.flip(super().getImageArray(), self.direction)

class BlurredWebcamSupplier(WebcamSupplier):
    
    def __init__(self, width, height, amount=(5, 5)):
        super().__init__(width, height)
        self.amount = amount

    def getImageArray(self):
        return cv2.blur(super().getImageArray(), self.amount)


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

    def getImage(self):
        buffer = np.full((self.width, self.height, 3), self.getColor(), dtype=np.uint8)
        return QImage(buffer, self.width, self.height, QImage.Format_RGB888)
