import sys

from PyQt5.QtWidgets import QMainWindow

from .tab_manager import TabManager

class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()

        # member variables
        self.tabManager = TabManager(self)

        # setup window
        self.setWindowTitle("qtbooth")
        self.setCentralWidget(self.tabManager)
