import cv2
from suppliers import WebcamSupplier

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