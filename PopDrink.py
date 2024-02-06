"""
    This class handles the attributes of drinks for Popcorn Machine™
"""

class PopDrink:

    aID         = ""
    aName       = ""
    aSize       = ""        # Either 'S', 'M' or 'AMERICAN'
    aFlavour    = ""
    aAddedSugar = False

    def __init__(self, aID, aNam, aSiz, aFla, aAdS):
        self.aID         = aID
        self.aName       = aNam
        self.aSize       = aSiz
        self.aFlavour    = aFla
        self.aAddedSugar = aAdS