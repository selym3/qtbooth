from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

class ImageDisplay(QLabel):
    
    def __init__(self, supplier, filter=None):
        super().__init__()

        self.supplier = supplier
        self.filter = filter

        self.setAlignment(Qt.AlignCenter)

    def update(self, image, format):
        qImage = QImage(image, image.shape[1], image.shape[0], format)

        self.setPixmap(QPixmap.fromImage(qImage))