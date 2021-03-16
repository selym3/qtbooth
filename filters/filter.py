
from modifiers import *

class Filter:
    
    def __init__(self):
        """
        A filter should have a dictionary of modifiers.
        Modifiers allow the user to modify internal 
        parameters of a filter. 
        
        They must be in this dictionary so that they
        can be added to the tab
        """
        
        self.modifiers = {
            # "example" : Modifier()
        }

    def filter(self, image):
        """
        Should apply a 'filter' to an image, without
        modifying it. 
        
        A filter can change the values in the pixels, the size,
        and the format of an image.
        """
        
        return image