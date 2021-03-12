import cv2

from modifiers import (NumberModifier, BooleanModifier)

class TestFilter:


    def __init__(self):

        self.modifiers = {
            "inverted": NumberModifier("Inverted", -2, 1, default=-2),
            "blur": NumberModifier("Blur", 0, 10)
        }

    def filter(self, image):

        inverted, blur = self.modifiers["inverted"], self.modifiers["blur"]

        if inverted.getValue() != -2:
            image = cv2.flip(image, inverted.getValue())
        
        if blur.getValue() != 0:
            amount = blur.getValue()
            image = cv2.blur(image, (amount, amount))

        return image