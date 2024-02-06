"""
    This class creates a Popcorn Machine™ that lets Users buy popcorn and drinks.
    Right now it's a magical machine that 'just works' and creates things out of thin air.
    If we want to we can make it more complex later and code its actual functionality.

    Warning: As the magic source of Popcorn Machine™ is unknown, DO NOT create anything but popcorn or drinks.
             DO NOT use Popcorn Machine™ to create living beings.
             DO NOT use Popcorn Machine™ to create world ending devices.
"""

class PopcornMachine:

    aID        = ""
    aPopMenu   = []
    aDrinkMenu = []

    def __init__(self, aID, aPoM, aDrM):
        self.aID        = aID
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



# ============================================= Franke's Code Starts Here =============================================




#check Vorrat
def chckStock():
    #Vorrat ist komplett vorhanden
    print("Vorrat pass")


#Anzeige Menu
def popcornMenu():
    offer_popcorn = ["gross-suess",  "mittel-suess", "klein-suess", "gross-salzig", "mittel-salzig", "klein-salzig"]
    print (*list(enumerate(offer_popcorn, start = 1)),  sep="\n")

#Auswahl Menu / Uebergabe an Maschine
def choosePopcorn():
    order = input("Welches Popkorn moechten Sie?: ")
    if order == "1":
        print("gross-suess an Maschine uebergeben")
    elif order == "2":
        print("mittel-suess an Maschine uebergeben")
    elif order == "3":
        print("klein-suess an Maschine uebergeben")
    elif order == "4":
        print("gross-salzig an Maschine uebergeben")
    elif order == "5":
        print("mittel-salzig an Maschine uebergeben")
    elif order == "6":
        print("klein-salzig an Maschine uebergeben")
    else:
        print("falsche Eingabe -- Abbruch, Hauptmenu")

#Uebergabe an Maschine
def order2Maschine():
    pass

#Anzeige von Info von Maschine, dass Popcorn fertig
def outputTray():
    print("Bitte Fach 3 oeffnen.")

#Aktion Fach oeffnen
def openTray():
    input("Fachnummer 3 oeffnen")

#Kundenkonto belasten
def billing():
    pass
