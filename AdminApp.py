"""
    This module handles all organisational stuff
    Things like add new items to the Popcorn Machine™ menu or changing the movie program
    While App is the interface for Users, AdminApp is the interface for whoever runs the cinema

    With this app, the owner can:
        >create instances of:
            >Cinema
            >Movie
            >MovieProgram
            >PopcornMachine
            >PopDrink
            >PopPopcorn
            >Theater
            >>Instances of User will NOT be created here but in App
            >>Instances of any class are stored externally in a JSON file
        >Change attributes of movies
        >Change the movie program

    Potential future functionality:
        >delete/ban a user

    General functionality:
        >organized function that lets admin create instances of classes

    TODO:
        >Graphical Interface
        >Find a way to convert the saved instances in JSON back into real instances of classes
"""
import json

import Cinema as cin
import PopcornMachine
import Tools


def create_cinema(aID, aNam, aLoc, aAmT) -> None:
    file = "saved_classes/cinema.json"
    inst = {"aID":aID, "aNam":aNam, "aLoc":aLoc, "aAmT":aAmT}
    cate = "cinemas"

    Tools.write_to_file(file, inst, cate)

def create_movie(aID, aNam, aLen, aGen, aPri, aReD, aAgR, aStR, a2D, a3D, aDes) -> None:
    file = "saved_classes/movie.json"
    inst = {"aID":aID,   "aNam":aNam, "aLen":aLen, "aGen":aGen, "aPri":aPri,
            "aReD":aReD, "aAgR":aAgR, "aStR":aStR, "a2D":a2D  , "a3D":a3D,   "aDes":aDes}
    cate = "movies"

    Tools.write_to_file(file, inst, cate)

def create_movie_program(aID, aCin, aMoL) -> None:
    file = "saved_classes/movie_program.json"
    inst = {"aID":aID, "aCin":aCin, "aMoL":aMoL}
    cate = "moviePrograms"

    Tools.write_to_file(file, inst, cate)

# Making a new popcorn machine only need aID as input
# The menus for drinks and popcorns were already populated in create_pop_drink() and create_pop_popcorn()
def create_popcorn_machine(aID) -> None:
    aPoM = PopcornMachine.create_popcorn_menu()
    aDrM = PopcornMachine.create_drink_menu()

    file = "saved_classes/popcorn_machine.json"
    inst = {"aID":aID, "aPoM":aPoM, "aDrM":aDrM}
    cate = "popcornMachines"

    Tools.write_to_file(file, inst, cate)

def create_pop_drink(aID, aNam, aSiz, aFla, aAdS) -> None:
    file = "saved_classes/pop_drink.json"
    inst = {"aID":aID, "aNam": aNam, "aSiz":aSiz, "aFla":aFla, "aAdS":aAdS}
    cate = "drinks"

    Tools.write_to_file(file, inst, cate)

def create_pop_popcorn(aID, aNam, aSiz, aFla) -> None:
    file = "saved_classes/pop_popcorn.json"
    inst = {"aID":aID, "aNam":aNam, "aSiz":aSiz, "aFla":aFla}
    cate = "popcornTypes"

    Tools.write_to_file(file, inst, cate)

def create_theater(aID, aNam, aMax, aCur, aSeM) -> None:
    file = "saved_classes/theater.json"
    inst = {"aID":aID, "aNam":aNam, "aMax":aMax, "aCur":aCur, "aSeM":aSeM}
    cate = "theaters"

    Tools.write_to_file(file, inst, cate)


def change_movie_program(aID, aCin=None, aMoL=None):
    pass