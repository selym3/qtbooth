import cv2
from PyQt5.QtGui import QImage
from modifiers import BooleanModifier, NumberModifier

class WebcamSupplier:
    
    CAMERA_INSTANCE = None

    def updateCamera():
        if WebcamSupplier.CAMERA_INSTANCE is None:
            WebcamSupplier.CAMERA_INSTANCE = cv2.VideoCapture(0)

        camera = WebcamSupplier.CAMERA_INSTANCE

        if camera is None or not camera.isOpened():
            raise Exception("Default video capture could not be opened! It may already be in use.")        

        return camera

    def __init__(self, width, height):
        self.width, self.height = width, height

        self.webcam = WebcamSupplier.updateCamera()

        self.modifiers = [ 
            BooleanModifier("Inverted", False), 
            NumberModifier("Blur", 1, 10) 
        ] 

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