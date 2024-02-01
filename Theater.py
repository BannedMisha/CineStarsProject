"""
    This class handles the attributes of theaters in our cinema
"""


class Theater:

    aName        = ""
    aMaxCapacity = 0
    aCurCapacity = 0
    aSeatMatrix  = [[],           # Shows a matrix of available seats in a theater
                   [],            # It only sounds complicated because it is
                   []]

    def __init__(self,aNam,aMax,aCur,aSeM):
        self.aName        = aNam
        self.aMaxCapacity = aMax
        self.aCurCapacity = aCur
        self.aSeatMatrix  = aSeM

    # getter/setter methods
    def set_theater_info(self):
        pass

    def get_theater_info(self):
        pass