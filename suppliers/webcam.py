import cv2
from PyQt5.QtGui import QImage

from .image_format import BGR_8

class WebcamSupplier:
    
    CAMERA_INSTANCE = None

    def getCamera():
        if WebcamSupplier.CAMERA_INSTANCE is None:
            WebcamSupplier.CAMERA_INSTANCE = cv2.VideoCapture(0)

        camera = WebcamSupplier.CAMERA_INSTANCE

        if camera is None or not camera.isOpened():
            raise Exception("Default video capture could not be opened! It may already be in use.")        

        return camera

    def __init__(self, width, height):
        self.width, self.height = width, height

        self.webcam = WebcamSupplier.getCamera()

    def getImageArray(self):
        ret, frame = self.webcam.read()
        frame = cv2.resize(frame, (self.width, self.height), interpolation=cv2.INTER_LANCZOS4)

        return frame

    def getImage(self):
        return self.getImageArray(), BGR_8 # QImage.Format_BGR888