from PyQt5.QtGui import QImage
import numpy as np

from .image_format import RGB_8

class Supplier:
    
    def getImage(self):
        """
        A supplier needs to return a numpy array 
        that represents the image, and a format.
        """

        return np.zeros((240, 320, 3), dtype=np.uint8), RGB_8 # QImage.Format_RGB888