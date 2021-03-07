from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QPushButton
from .tab import Tab

class TabManager(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.tabCount = 1 # <- for good default names

        # Create root layout
        self.layout = QVBoxLayout(self)

        # Create base components
        self.tabs = QTabWidget()
        self.cornerButton = QPushButton("+")

        # Use root layout
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        # Initialization
        self._addNewTab()

        # add the change listeners after all changes have been made
        self.tabs.tabBar().setTabsClosable(True)
        self.tabs.tabBar().tabCloseRequested.connect(self._removeTab)

        self.tabs.tabBar().setMovable(True)

        self.tabs.setCornerWidget(self.cornerButton)
        self.cornerButton.clicked.connect(self._addNewTab)

    def _addNewTab(self):
        self._addTab(self.tabs.count() - 2, f"New tab ({self.tabCount})", True)
        self.tabCount += 1

    def _addTab(self, index, label, focus=False):

        newTab = Tab(self, label)
        newTab.index = self.tabs.insertTab(index, newTab, label)

        self._updateIndices()

        if focus:
            self.tabs.setCurrentIndex(newTab.index)

    def _updateIndices(self):
        for i in range(self.tabs.count()):
            self.tabs.widget(i).index = i

    def _hasTabs(self):
        return self.tabs.count() > 0

    def _removeTab(self, idx=0):
        # this accouns for the last tab being protected (which it should be)
        if idx < 0 or idx >= self.tabs.count():
            return 
        if self.tabs.count() == 1:
            return
        
        self.tabs.removeTab(idx)
        self._updateIndices()