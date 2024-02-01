"""
    This class handles the attributes of popcorn for Popcorn Machine™
"""


class PopDrink:
    aSize    = ""       # Either 'S', 'M' or 'AMERICAN'
    aFlavour = ""       # Sweet, Salty or Mixed

    def __init__(self, aSiz, aFla, aAdS):
        self.aSize    = aSiz
        self.aFlavour = aFla