"""
    This class handles Tickets
"""

# Needs MovieProgram ID, Theater ID, Week (current or next), Day and Movie as input

class Ticket:
    aID            = ""
    aCinema        = ""

    def __init__(self,aID, aCin):
        self.aID            = aID
        self.aCinema        = aCin