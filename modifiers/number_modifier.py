from PyQt5.QtWidgets import QLabel, QSlider
from PyQt5.QtCore import Qt

class NumberModifier:
    
    def __init__(self, name, low, high, interval=1, default=None):
        # Setup label
        label = QLabel(name)

        # Setup slider
        slider = QSlider(Qt.Horizontal)
        slider.setRange(low, high)
        slider.setValue(low)
        slider.setTickInterval(interval)

        slider.valueChanged[int].connect(self.setValue)

        if default is None:
            default = low
        
        self.value = default


        self.components = [ label, slider ]

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value