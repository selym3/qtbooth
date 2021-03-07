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
        self.tabs.tabBar().tabMoved.connect(self._updateIndices)

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
        if idx < 0 or idx >= self.tabs.count() or self.tabs.count() <= 1:
            return 
        
        self._closeTab(idx)
        self.tabs.removeTab(idx)
        self._updateIndices()

    def _pauseTabs(self):
        for i in range(self.tabs.count()):
            tab = self.tabs.widget(i)
            tab.setStreaming(False)

    def _closeTab(self, idx):
        tab = self.tabs.widget(idx) 
        tab.close()

    def closeTabs(self):
        for i in range(self.tabs.count()):
            self._closeTab(i)