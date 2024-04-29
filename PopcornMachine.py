"""
    This class creates a Popcorn Machine™ that lets Users buy popcorn and drinks.
    Right now it's a magical machine that 'just works' and creates things out of thin air.
    If we want to we can make it more complex later and code its actual functionality.

    Warning: As the magic source of Popcorn Machine™ is unknown, DO NOT create anything but popcorn or drinks.
             DO NOT use Popcorn Machine™ to create living beings.
             DO NOT use Popcorn Machine™ to create world ending devices.
"""

import Tools


# This function creates the popcorn menu
# The list is populated by the names (aNam) from all entries of pop_popcorn.json
def create_popcorn_menu():
    popList = Tools.read_multiple_from_file("saved_classes/pop_popcorn.json", "popcornTypes", "aNam")
    return popList


# This function creates the drinks menu
# The list is populated by the names (aNam) from all entries of pop_drinks.json
def create_drink_menu():
    driList = Tools.read_multiple_from_file("saved_classes/pop_drink.json", "drinks", "aNam")
    return driList


#
#       AD OVERLOADED DISPATCH FUNCTION HERE, ACCEPT EITHER DRINK OR POPCORN
#       RECURSION????
#       MAKE THIS A SINGLETON
#       __STR__ ÜBERLADEN
#       deep and shallow copies
#


"""
    Add more stuff below this point here. Make it cool. Add whatever functionality could work for a Popcorn Machine.
    Real functional code, not pseudocode.
"""


# This function makes the popcorn
# Popcorn is being magically created
# Then the tray opens and closes after a set time or until the customer took out their item
def prepare_popcorn():
    print("\n***\n> Popcorn has been created!\n***\n")

# Same for drinks
def prepare_drinks():
    print("\n***\n> Drink has been created!\n***\n")
