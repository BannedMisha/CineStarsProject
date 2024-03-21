"""
    The class App controls most parts of the functionality for the User

    Everything in here is controlled via an app the user can control with their phone
"""

import json
import Tools
import PopcornMachine

loggedIn = False    # Boolean to track if the user is logged in or not

"""
========================================================================================================================

    This block contains all the functionality for the user to control what they can do during their cinema visit
    You can think of these as "buttons" the user can press on their phone within the app to do stuff
    > Buy ticket
    > Cancel Ticket (NYI)
    > Show the movie program of either this week or next week (also displays available seats (NYI))
    > Buy popcorn
    > Buy drinks
    > Display popcorn menu
    > Display drinks menu
    > Create a wishlist of all the movies the user still wants to watch (NYI)
    > Display the wishlist (NYI)

========================================================================================================================
"""

# Lets the User buy a ticket
# thisWeek : boolean, True for current week, False for next week
# day      : string, name of the day (e.g. "WED")
# movieID  : string, ID of the movie the user wants to buy the ticket of
def buy_ticket(thisWeek, day, movieID) -> bool:
    movie = Tools.convert_id_to_name("saved_classes/movie.json", "movies", movieID)
    ticketBought = Tools.ticket_buyer(thisWeek, day, movieID)

    if ticketBought:
        print(f"Your ticket for the movie {movie} on {day} has been successfully booked.")
    else:
        print("Sorry, buddy, no more tickets. Get the frick outta here.")

    return ticketBought

# Lets the User cancel the ticket
# Returns True if ticket has been cancelled succesfully, False if not
def cancel_ticket()-> bool:
    pass

# Returns a list of the movie program
# ID       : the ID of the specific class instance we want the content from (E.g. "MP0002")
# thisWeek : boolean, True for current week, False for next week
def show_program(ID, thisWeek) -> list:
    movieProgram = Tools.show_movie_list(ID, thisWeek)

    return movieProgram

# Lets the User buy popcorn at the Popcorn Machine™
# First presents user with a list of the popcorn menu
# Then user can pick one item from the list
# The Popcorn Machine™ creates the popcorn and opens the tray, then closes it after a set time (in PopcornMachine)
# ID       : the ID of the specific class instance we want the content from (E.g. "MP0002")
def buy_popcorn(ID) -> None:
    popcornList = Tools.read_from_file("saved_classes/popcorn_machine.json",
                                   "popcornMachines",ID,"aPoM")

    for index,item in enumerate(popcornList):
        print(f"{index}:{item}")

    uInput = input("Pick your item: ")

    print(f"You picked: {uInput}")
    PopcornMachine.prepare_popcorn()


# Same as buy_popcorn() just with drinks
# Can choose between a few different drinks and sizes
# ID       : the ID of the specific class instance we want the content from (E.g. "MP0002")
def buy_drink(ID) -> None:
    drinkList = Tools.read_from_file("saved_classes/popcorn_machine.json",
                                       "popcornMachines", ID, "aDrM")

    for index, item in enumerate(drinkList):
        print(f"{index}:{item}")

    uInput = input("Pick your item: ")

    print(f"You picked: {uInput}")
    PopcornMachine.prepare_drinks()

# Lets the user see the popcorn menu
# ID       : the ID of the specific class instance we want the content from (E.g. "MP0002")
def show_popcorn(ID) -> None:
    popcorn = Tools.read_from_file("saved_classes/popcorn_machine.json",
                                   "popcornMachines",ID,"aPoM")
    print(popcorn)

# Lets the user see the drinks menu
# ID       : the ID of the specific class instance we want the content from (E.g. "MP0002")
def show_drinks(ID) -> None:
    drinks = Tools.read_from_file("saved_classes/popcorn_machine.json",
                                   "popcornMachines",ID,"aDrM")
    print(drinks)


# Lets User create a wishlist of the movies they want to see in the future
def create_wishlist():
    pass

# And returns that very list
def show_wishlist():
    pass



""" 
========================================================================================================================

    This block contains all the functionality that is related to the user's json entry
    These are also "buttons" within the functionality of the app
    > create account
    > delete account
    > edit account
    > login
    > logout
    
========================================================================================================================
"""

# In this function the User can create their account
# Like the create functions in AdminApp, this needs all the user's attributes as input
def create_user_account(aID, aNam, aFiN, aLaN, aBiD, aEma, aPas) -> None:
    file = "saved_classes/user.json"
    inst = {"aID":aID, "aNam":aNam, "aFiN":aFiN, "aLaN":aLaN, "aBiD":aBiD, "aEma":aEma, "aPas":aPas}
    cate = "users"

    Tools.add_entry_to_file(file, inst, cate)

# Function to delete the user's account
# Uses the delete_entry_from_file() function from Tools.py, for more information, look there
# We secretly keep all the data and sell them to China. Of course.
def delete_user_account(aID):
    file = "saved_classes/user.json"
    cate = "users"

    Tools.delete_entry_from_file(file, cate, aID)

# Function to edit the user's account
# Needs inputs for all the Users attributes, otherwise they will be overwritten with "nothing"
# Uses the edit_entry_from_file() function from Tools.py, for more information, look there
def edit_user_account(ID, aNam, aFiN, aLaN, aBiD, aEma, aPas) -> None:
    file = "saved_classes/user.json"
    inst = {"aNam": aNam, "aFiN": aFiN, "aLaN": aLaN, "aBiD": aBiD, "aEma": aEma, "aPas": aPas}
    cate = "users"

    Tools.edit_entry_from_file(file, inst, cate, ID)

# Function to let the user log into their account
# To log in the user needs to provide their credentials (account name/email address + password)
# If successfully logged in, the global variable loggedIn switches to True
def login_account(aAcN, aPas):
    global loggedIn

    if loggedIn:
        print("You're already logged in, so you shouldn't be able to see this.")
    else:
        file = "saved_classes/user.json"

        with open(file) as jFile:
            data = json.load(jFile)

        for entry in data["users"]:
            if entry.get("aAcN") == aAcN and entry.get("aPas") == aPas:
                loggedIn = True
                print("Login successful")
            else:
                print("Error: Password or Username don't match")


# Function to let the user log out of their account
# If successfully logged out, the global variable loggedIn switches to False
def logout_account():
    global loggedIn

    if loggedIn:
        loggedIn = False
        print("You successfully logged out")
    else:
        print("You're not logged in, so you shouldn't even be able to see this.")