
import cv2

from modifiers import NumberModifier
from suppliers import image_format

class ThresholdFilter:

    def __init__(self):

        self.modifiers = {
            "min_hue": NumberModifier("Min Hue", 0, 180, default=0),
            "max_hue": NumberModifier("Max Hue", 0, 180, default=180),
            "min_sat": NumberModifier("Min Saturation", 0, 255, default=0),
            "max_sat": NumberModifier("Max Saturation", 0, 255, default=255),
            "min_val": NumberModifier("Min Value", 0, 255, default=0),
            "max_val": NumberModifier("Max Value", 0, 255, default=255)
        }

    def filter(self, image):

        buffer, format = image

        hsv_image = format.convertImage(buffer, 'HSV')
        binary_image = cv2.inRange(hsv_image, self.min_threshold(), self.max_threshold())

        contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        largest = self.largest_contour(contours)

        buffer = format.convertImage(buffer, 'RGB')

        if not largest is None:
            cv2.drawContours(buffer, [ largest ], -1, 255, 3)

        return buffer, format


    def min_threshold(self):
        return self.modifiers["min_hue"].getValue(), self.modifiers["min_sat"].getValue(), self.modifiers["min_val"].getValue()

    def max_threshold(self):
        return self.modifiers["max_hue"].getValue(), self.modifiers["max_sat"].getValue(), self.modifiers["max_val"].getValue()
    
    def largest_contour(self, contours):
        if len(contours) <= 0:
            return None

        largest = contours[0]

        for contour in contours:
            if cv2.contourArea(contour) > cv2.contourArea(largest):
                largest = contour

        return largest