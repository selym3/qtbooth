import sys

from PyQt5.QtWidgets import QMainWindow

from PyQt5.QtCore import Qt

from .tab_manager import TabManager

class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()

        # member variables
        self.tabManager = TabManager(self)

        # setup window
        self.setWindowTitle("qtbooth")
        self.setCentralWidget(self.tabManager)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        elif event.key() == Qt.Key_Space:
            self._toggleActiveTab()

    def _toggleActiveTab(self):
        # TODO: add better gettets
        self.tabManager.activeTab().toggle()

    def closeEvent(self, *args, **kwargs):
        self.tabManager.closeTabs()
        print("Closing")