
from PyQt5.QtWidgets import QCheckBox

class BooleanModifier:
    
    def __init__(self, name, default=False):
        checkBox = QCheckBox(name)
        checkBox.setChecked(default)
        
        self.components = [ checkBox ]

    def isOn(self):
        return self.components[0].isChecked()