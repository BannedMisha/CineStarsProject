"""
    This class creates a Popcorn Machine™ that lets Users buy popcorn and drinks.
    Right now it's a magical machine that 'just works' and creates things out of thin air.
    If we want to we can make it more complex later and code its actual functionality.

    Warning: As the magic source of Popcorn Machine™ is unknown, DO NOT create anything but popcorn or drinks.
             DO NOT use Popcorn Machine™ to create living beings.
             DO NOT use Popcorn Machine™ to create world ending devices.
"""

class PopcornMachine:

    aPopMenu   = []
    aDrinkMenu = []

    def __init__(self,aPoM,aDrM):
        self.aPopMenu   = aPoM
        self.aDrinkMenu = aDrM

    # Getter/Setter Methods
    def set_pop_menu(self):
        pass

    def set_drink_menu(self):
        pass

    def get_pop_menu(self):
        pass

    def get_drink_menu(self):
        pass

    # Pops popcorn and dispenses it to hungry user
    def make_popcorn(self):
        pass

    # Fills up a cup of a choice beverage and dispenses it to the user
    def make_drink(self):
        pass