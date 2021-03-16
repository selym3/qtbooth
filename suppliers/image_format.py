"""
A format for a supplier that provides a gateway 
between QImage formats and OpenCV formats
"""

from PyQt5.QtGui import QImage
import cv2

class Format:

    def __init__(self, format, name):
        self._format = format
        self._name = name

    def toQImage(self):
        return self._format

    def convertTo(self, other): 
        # TODO: This will not work for all conversions
        nameOf = f"COLOR_{self._name}2{other}"
        return getattr(cv2, nameOf, None)

    def convertImage(self, buffer, format):
        format = self.convertTo(format)
        if format is None:
            return buffer

        return cv2.cvtColor(buffer, format)

RGB_8 = Format(QImage.Format_RGB888, 'RGB')
RGBA_8 = Format(QImage.Format_RGBA8888, 'RGBA')
BGR_8 = Format(QImage.Format_BGR888, 'BGR')