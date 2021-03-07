
from PyQt5.QtWidgets import QWidget, QScrollArea, QGroupBox, QPushButton, QFormLayout, QLineEdit
from .image_display import ImageDisplay
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
        self.imageSupplier = WebcamSupplier(1920, 1080) # ImageSupplier('resources/car.jpg')
        self.image = ImageDisplay(self.imageSupplier)

        self.rootLayout.addWidget(self.image)

        updateButton = QPushButton("Update Button")
        updateButton.clicked.connect(self.image.update)

        self.rootLayout.addWidget(updateButton)

        self.tabName = QLineEdit()
        self.tabName.setText(name)

        self.rootLayout.addWidget(self.tabName)

        button = QPushButton("Set Tab Name")
        button.clicked.connect(self.updateName)

        self.rootLayout.addWidget(button)

        ################

        self.setWidget(self.rootBox)
        self.setWidgetResizable(True)

        # self.setLayout(self.layout)

    def updateName(self):
        # print(self.index)
        self.tabManager.tabs.setTabText(self.index, self.tabName.text())

    