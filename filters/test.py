import cv2

from modifiers import (NumberModifier, BooleanModifier)

class TestFilter:


    def __init__(self):

        self.modifiers = {
            "inverted": NumberModifier("Inverted", -2, 1, default=-2),
            "blur": NumberModifier("Blur", 0, 10)
        }

    def filter(self, image):

        buffer, format = image

        inverted, blur = self.modifiers["inverted"], self.modifiers["blur"]

        if inverted.getValue() != -2:
            buffer = cv2.flip(buffer, inverted.getValue())
        
        if blur.getValue() != 0:
            amount = blur.getValue()
            buffer = cv2.blur(buffer, (amount, amount))

        return buffer, format