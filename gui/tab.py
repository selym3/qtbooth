
from PyQt5.QtWidgets import (QScrollArea, QGroupBox, QPushButton, QFormLayout, QLineEdit)

from display import *
from suppliers import *
from filters import *

class Tab(QScrollArea):

    def __init__(self, parent, name):
        super().__init__(parent)
        self.tabManager = parent

        # standard data

        self.index = -1

        # window manager stuff

        self.rootBox = QGroupBox()
        self.rootLayout = QFormLayout()
        self.rootBox.setLayout(self.rootLayout)

        ### ADD HERE ###
        # supplier = WebcamSupplier(320, 240)
        # supplier = ColorSupplier((0, 255, 0), 320, 240)
        supplier = ImageSupplier('resources/car.jpg', (320, 240))
        # supplier = ImageSupplier('resources/test.jpg')
        # supplier = RainbowSupplier(0.001, 340, 240)
        
        filter = ThresholdFilter()
        # filter = TestFilter()
        
        self.image = ImageDisplay(supplier, filter)
        self.stream = DisplayThread(self.image, 50)

        self.rootLayout.addWidget(self.image)

        for modifier in filter.modifiers.values():
            for widget in modifier.components:
                self.rootLayout.addWidget(widget)

        pauseButton = QPushButton("Toggle Playback")
        pauseButton.clicked.connect(self.toggle)

        self.rootLayout.addWidget(pauseButton)

        # updateButton = QPushButton("Update Button")
        # updateButton.clicked.connect(self.image.update)

        # self.rootLayout.addWidget(updateButton)

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

    def isStreaming(self):
        return not self.stream.paused

    def close(self):
        # self.image.supplier.clearModifiers()

        self.stream.running = False
        self.stream.join()
        self.stream = None

    def toggle(self):
        pausedState = self.isStreaming()
  
        self.tabManager._pauseTabs()
        self.stream.paused = pausedState

    def updateName(self):
        text = self.tabName.text()
        self.tabManager.tabs.setTabText(self.index, text)
        # self.image.supplier = self.getSupplier(text)

    # def getSupplier(self, name):
    #     supplier = ColorSupplier((0, 0, 255), 320, 240)
    #     if name == "webcam":
    #         supplier = WebcamSupplier(320, 240)
    #     elif name.startswith('webcam-'):
    #         try:
    #             direction = name[len('webcam-'):]
    #             supplier = FlippedWebcamSupplier(320, 240, int(direction))
    #         except Exception as e:
    #             pass
    #     elif name == 'blur':
    #         supplier = BlurredWebcamSupplier(320, 240)
    #     elif name.startswith('blur-'):
    #         try:
    #             amount = name[len('blur-'):]
    #             amount = int(amount)
    #             supplier = BlurredWebcamSupplier(320, 240,(amount, amount))
    #         except Exception as e:
    #             supplier = BlurredWebcamSupplier(320, 240)
    #     else:
    #         pass
    #     return supplier