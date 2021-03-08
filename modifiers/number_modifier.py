from PyQt5.QtWidgets import QLabel, QSlider
from PyQt5.QtCore import Qt

class NumberModifier:
    
    def __init__(self, name, low, high, interval=1):
        # Setup label
        label = QLabel(name)

        # Setup slider
        slider = QSlider(Qt.Horizontal)
        slider.setRange(low, high)
        slider.setValue(low)
        slider.setTickInterval(interval)

        slider.valueChanged[int].connect(self.setValue)

        self.value = low


        self.components = [ label, slider ]

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value