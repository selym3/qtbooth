import sys

from PyQt5.QtWidgets import QApplication
from gui import Window

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = Window()
    
    # width, height = 640, 480
    # window.setMinimumSize(width, height)
    
    window.show()

    sys.exit(app.exec_())