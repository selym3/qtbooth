
from PyQt5.QtWidgets import (QScrollArea, QGroupBox, QPushButton, QFormLayout, QLineEdit, QComboBox)

from display import *
from suppliers import *
from filters import *

class Tab(QScrollArea):

    SUPPLIERS = {
        "None": Supplier(),
        "Webcam": WebcamSupplier(320, 240), 
        "A Color": ColorSupplier((0, 255, 0), 320, 240),
        "A Rainbow": RainbowSupplier(0.01, 320, 240),
        "Image": ImageSupplier('resources/car.jpg', (320, 240))
    }

    def __init__(self, parent, name):
        super().__init__(parent)
        self.tabManager = parent

        # standard data

        self.index = -1

        # window manager stuff

        self.rootBox = QGroupBox()
        self.rootLayout = QFormLayout()
        self.rootBox.setLayout(self.rootLayout)

        # supplier dropdown

        supplierDropdown = QComboBox(self)

        for supplierName in Tab.SUPPLIERS:
            supplierDropdown.addItem(supplierName)
        
        supplierDropdown.activated[str].connect(self.changeSupplier)

        self.rootLayout.addWidget(supplierDropdown)

        ### ADD HERE ###
        supplier = Tab.SUPPLIERS["None"] # WebcamSupplier(320, 240)
        # supplier = ColorSupplier((0, 255, 0), 320, 240)
        # supplier = ImageSupplier('resources/car.jpg', (320, 240))
        # supplier = ImageSupplier('resources/test.jpg')
        # supplier = RainbowSupplier(0.001, 340, 240)
        
        # filter = Filter()
        # filter = ThresholdFilter()
        filter = TestFilter()

        # actual image display

        self.image = ImageDisplay(supplier, filter)
        self.stream = DisplayThread(self.image, 50)

        self.rootLayout.addWidget(self.image)

        # add the components for a filter's modifiers

        for modifier in filter.modifiers.values():
            for widget in modifier.components:
                self.rootLayout.addWidget(widget)

        # add a pause button

        self.pauseButton = QPushButton(self.getToggleText())
        self.pauseButton.clicked.connect(self.toggle)

        self.rootLayout.addWidget(self.pauseButton)

        # add a tab name input

        self.tabName = QLineEdit()
        self.tabName.setText(name)

        self.rootLayout.addWidget(self.tabName)

        button = QPushButton("Set Tab Name")
        button.clicked.connect(self.updateName)

        self.rootLayout.addWidget(button)

        ################

        self.setWidget(self.rootBox)
        self.setWidgetResizable(True)

        self.stream.start()

        # self.setLayout(self.layout)

    def setStreaming(self, isStreaming):
        self.stream.paused = not isStreaming
        self.pauseButton.setText(self.getToggleText())

    def isStreaming(self):
        return not self.stream.paused

    def changeSupplier(self, text):
        self.image.supplier = Tab.SUPPLIERS[text]

    def close(self):
        self.stream.running = False
        self.stream.join()
        self.stream = None

    def getToggleText(self):
        return "Pause" if self.isStreaming() else "Play"

    def toggle(self):
        pausedState = self.isStreaming()

        self.tabManager._pauseTabs()
        self.setStreaming(not pausedState)

    def updateName(self):
        text = self.tabName.text()
        self.tabManager.tabs.setTabText(self.index, text)