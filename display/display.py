from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class ImageDisplay(QLabel):
    
    def __init__(self, supplier):
        super().__init__()

        self.supplier = supplier
        
        self.setAlignment(Qt.AlignCenter)

        # do one update on initialize
        self.update()

    def update(self):
        image = self.supplier.getImage()

        self.setPixmap(QPixmap.fromImage(image))