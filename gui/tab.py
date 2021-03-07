
from PyQt5.QtWidgets import QWidget, QScrollArea, QGroupBox, QPushButton, QFormLayout, QLineEdit
from .image_display import ImageDisplay, DisplayThread
from .image_suppliers import ColorSupplier, RainbowSupplier, ImageSupplier, WebcamSupplier

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
        # self.imageSupplier = WebcamSupplier(320, 240)
        self.imageSupplier = ImageSupplier('resources/car.jpg')
        # self.imageSupplier = ImageSupplier('resources/test.jpg') 
        # self.imageSupplier = RainbowSupplier(0.001, 340, 240)# WebcamSupplier(320, 240) # 
        self.image = ImageDisplay(self.imageSupplier)
        self.imageRunner = DisplayThread(self.image, 50)

        self.rootLayout.addWidget(self.image)

        pauseButton = QPushButton("Toggle Playback")
        pauseButton.clicked.connect(self._toggleImageStream)

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

        self.imageRunner.start()

        # self.setLayout(self.layout)

    def close(self):
        self.imageRunner.running = False
        self.imageRunner.join()
        self.imageRunner = None

    def _toggleImageStream(self):
        self.imageRunner.paused = not self.imageRunner.paused

    def updateName(self):
        # print(self.index)
        self.tabManager.tabs.setTabText(self.index, self.tabName.text())

    