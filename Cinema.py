"""
    This class handles the attributes of our cinemas
    Right now we only have one cinema, if we implement it now, it's expandable. Which is nice.
"""

class Cinema:

    aID             = ""
    aName           = ""
    aLocation       = ""
    aAmountTheaters = 0

    def __init__(self, aID, aNam, aLoc, aAmT):
        self.aID             = aID
        self.aName           = aNam
        self.aLocation       = aLoc
        self.aAmountTheaters = aAmT

    # getter/setter methods
    def set_cinema_info(self):
        pass

    def get_cinema_info(self):
        pass