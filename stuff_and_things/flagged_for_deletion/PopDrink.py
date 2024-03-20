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






# ============================================= Franke's Code Starts Here =============================================






# check Vorrat
def chckStock():
    # Vorrat ist komplett vorhanden
    print("Vorrat pass")

# Anzeige Menu
def popdrinkMenu():
    offer_popdrink = ["Cola-gross", "Cola-klein", "Wasser-gross", "Wasser-klein", "Kaffee-gross", "Kaffee-klein"]
    print(*list(enumerate(offer_popdrink, start=1)), sep="\n")

# Auswahl Menu und Uebergabe an Maschine

def choosePopdrink():
    order = input("Welches Getraenk moechten Sie?: ")
    if order == "1":
        print("Cola-gross an Maschine uebergeben")
    elif order == "2":
        print("Cola-klein an Maschine uebergeben")
    elif order == "3":
        print("Wasser-gross an Maschine uebergeben")
    elif order == "4":
        print("Wasser-klein an Maschine uebergeben")
    elif order == "5":
        print("Kaffee-gross an Maschine uebergeben")
    elif order == "6":
        print("Kaffee-klein an Maschine uebergeben")
    else:
        print("falsche Eingabe -- Abbruch, Hauptmenu")

# Uebergabe an Maschine
def order2Maschine():
    pass

# Anzeige von Info von Maschine, dass Popcorn fertig
def outputTray():
    print("Bitte Fach 3 oeffnen.")

# Aktion Fach oeffnen
def openTray():
    input("Fachnummer 3 oeffnen")

# Kundenkonto belasten
def billing():
    pass