"""
    This class handles the attributes of drinks for Popcorn Machine™
"""

class PopDrink:

    aSize       = ""        # Either 'S', 'M' or 'AMERICAN'
    aFlavour    = ""
    aAddedSugar = False

    def __init__(self,aSiz,aFla,aAdS):
        self.aSize       = aSiz
        self.aFlavour    = aFla
        self.aAddedSugar = aAdS