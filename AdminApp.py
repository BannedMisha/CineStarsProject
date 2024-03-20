"""
    This module handles all organisational stuff

    This can be seen as the software the owner uses to control their cinema
"""

import PopcornMachine
import Tools

"""
========================================================================================================================

    This block contains general functions the owner could use to run their cinema
    > Advance movie program to next week (NYI)

========================================================================================================================
"""

# This function copies next week's movie program to this week
# Then populates the movie program for next week
def movie_program_advance_week() -> None:
    pass



"""
========================================================================================================================

    This block contains all functions that handle entries inside their respective JSON files
    The owner can create, delete (NYI) and edit (NYI) the following:
    > Movie
    > Popcorn Machine
    > Drinks
    > Popcorn Flavours
    > Movie Program (theater)
    
    These functions take all the needed attributes as input, then create entries using the add_entry_to_file()
    functions that can be found in Tools.py
    
========================================================================================================================
"""
def create_movie(aID, aNam, aLen, aGen, aPri, aReD, aAgR, aStR, a2D, a3D, aDes) -> None:
    file = "saved_classes/movie.json"
    inst = {"aID":aID,   "aNam":aNam, "aLen":aLen, "aGen":aGen, "aPri":aPri,
            "aReD":aReD, "aAgR":aAgR, "aStR":aStR, "a2D":a2D  , "a3D":a3D,   "aDes":aDes}
    cate = "movies"

    Tools.add_entry_to_file(file, inst, cate)

def create_popcorn_machine(aID) -> None:
    aPoM = PopcornMachine.create_popcorn_menu()
    aDrM = PopcornMachine.create_drink_menu()

    file = "saved_classes/popcorn_machine.json"
    inst = {"aID":aID, "aPoM":aPoM, "aDrM":aDrM}
    cate = "popcornMachines"

    Tools.add_entry_to_file(file, inst, cate)

def create_pop_drink(aID, aNam, aSiz, aFla, aAdS) -> None:
    file = "saved_classes/pop_drink.json"
    inst = {"aID":aID, "aNam": aNam, "aSiz":aSiz, "aFla":aFla, "aAdS":aAdS}
    cate = "drinks"

    Tools.add_entry_to_file(file, inst, cate)

def create_pop_popcorn(aID, aNam, aSiz, aFla) -> None:
    file = "saved_classes/pop_popcorn.json"
    inst = {"aID":aID, "aNam":aNam, "aSiz":aSiz, "aFla":aFla}
    cate = "popcornTypes"

    Tools.add_entry_to_file(file, inst, cate)

def create_theater(aID, aNam, aMax, aPCW, aPNW) -> None:
    file = "saved_classes/theater.json"
    inst = {"aID":aID, "aNam":aNam, "aMax":aMax, "aPCW":aPCW, "aPNW":aPNW}
    cate = "theaters"

    Tools.add_entry_to_file(file, inst, cate)