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


def create_cinema(aID, aNam, aLoc, aAmT) -> None:
    file = "saved_classes/cinema.json"
    inst = {"aID":aID, "aNam":aNam, "aLoc":aLoc, "aAmT":aAmT}
    cate = "cinemas"

    write_to_file(file, inst, cate)

def create_movie(aID, aNam, aLen, aGen, aPri, aReD, aAgR, aStR, a2D, a3D, aDes) -> None:
    file = "saved_classes/movie.json"
    inst = {"aID":aID,   "aNam":aNam, "aLen":aLen, "aGen":aGen, "aPri":aPri,
            "aReD":aReD, "aAgR":aAgR, "aStR":aStR, "a2D":a2D  , "a3D":a3D,   "aDes":aDes}
    cate = "movies"

    write_to_file(file, inst, cate)

def create_movie_program(aID, aCin, aMoL) -> None:
    file = "saved_classes/movie_program.json"
    inst = {"aID":aID, "aCin":aCin, "aMoL":aMoL}
    cate = "moviePrograms"

    write_to_file(file, inst, cate)

def create_popcorn_machine(aID, aPoM, aDrM) -> None:
    file = "saved_classes/popcorn_machine.json"
    inst = {"aID":aID, "aPoM":aPoM, "aDrM":aDrM}
    cate = "popcornMachines"

    write_to_file(file, inst, cate)

def create_pop_drink(aID, aNam, aSiz, aFla, aAdS) -> None:
    file = "saved_classes/pop_drink.json"
    inst = {"aID":aID, "aNam": aNam, "aSiz":aSiz, "aFla":aFla, "aAdS":aAdS}
    cate = "drinks"

    write_to_file(file, inst, cate)

def create_pop_popcorn(aID, aNam, aSiz, aFla) -> None:
    file = "saved_classes/pop_popcorn.json"
    inst = {"aID":aID, "aNam":aNam, "aSiz":aSiz, "aFla":aFla}
    cate = "popcornTypes"

    write_to_file(file, inst, cate)

def create_theater(aID, aNam, aMax, aCur, aSeM) -> None:
    file = "saved_classes/theater.json"
    inst = {"aID":aID, "aNam":aNam, "aMax":aMax, "aCur":aCur, "aSeM":aSeM}
    cate = "theaters"

    write_to_file(file, inst, cate)


def change_movie_program(aID, aCin=None, aMoL=None):
    pass


# ============================= General Stuff =============================

# Function to save a classes attributes to their corresponding JSON file
# Better than to have duplicates of this functionality in each "create"-function
def write_to_file(file, instance, category):
    try:
        with open(file) as jFile:
            data = json.load(jFile)

        data[category].append(instance)

        with open(file, 'w') as wFile:
            json.dump(data, wFile, indent=4)

    except FileNotFoundError:
        print("ERROR: File not found")



# This function turns the information of a JSON file into a class, should probably not be in this module
# It picks the instance based on their ID ('aID')
# For now it only works for cinema, but that can be easily changed
# It doesn't really do much with the class instance either, but it works.
def class_instances_maker(file, aID):
    with open(file, 'r') as jFile:
        data = json.load(jFile)
        cinemas = data['cinemas']

        for cinema in cinemas:
            if cinema['aID'] == aID:
                aNam = cinema['aNam']
                aLoc = cinema['aLoc']
                aAmT = cinema['aAmT']

        new_cinema = cin.Cinema(aID, aNam, aLoc, aAmT)