from enum import Enum

from PyQt5.QtWidgets import QCheckBox, QLabel, QSlider
from PyQt5.QtCore import Qt

class BooleanModifier:

    def __init__(self, name, default=False):
        # self.name = name
        # self.default = default

        checkBox = QCheckBox(name)
        self.components = [ checkBox ]

    def isOn(self):
        return self.components[0].isChecked()

class NumberModifier:

    def __init__(self, name, low, high, interval=1):
        label = QLabel(name)

        slider = QSlider(Qt.Horizontal)
        slider.setRange(low, high)
        slider.setValue(low)
        slider.setTickInterval(interval)

        self.value = low

        slider.valueChanged[int].connect(self.setValue)

        self.components = [ label, slider ]

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value