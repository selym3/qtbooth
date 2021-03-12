from PyQt5.QtGui import QImage
import numpy as np

class Supplier:
    
    def getImage(self):
        """
        A supplier needs to return a numpy array 
        that represents the image, and a format.

        The format is limited to QImage format types,
        a class can be made to convert between OpenCV
        formats and QImage formats
        """

        return np.zeros((300, 300, 3), dtype=np.uint8), QImage.Format_RGB888