"""
    Class User handles all the attributes of our movie patrons
"""

class User:

    aID          = ""
    aAccountName = ""
    aFirstName   = ""
    aLastName    = ""
    aBirthDate   = ""       # variable type is date
    aEmail       = ""
    aPassword    = ""       # Probably don't want it to just exist like that as plain text ...

    def __init__(self,aID,aAcN,aFiN,aLaN,aBiD,aEma,aPas):
        self.aID          = aID
        self.aAccountName = aAcN
        self.aFirstName   = aFiN
        self.aLastName    = aLaN
        self.aBirthDate   = aBiD
        self.aEmail       = aEma
        self.aPassword    = aPas

    # getter/setter methods
    def set_user_info(self):
        pass

    def get_user_info(self):
        pass