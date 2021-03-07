from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class ImageDisplay(QLabel):

    def __init__(self, imageSupplier):
        super().__init__()

        self.imageSupplier = imageSupplier
        
        self.setAlignment(Qt.AlignCenter)

        # do one update on initialize
        self.update()
        # self.usedPixmap = False

    def update(self):
        image = self.imageSupplier.getImage()

        # if not self.usedPixmap:
            # self.setPixmap(QPixmap.fromImage())
        self.setPixmap(QPixmap.fromImage(image))

