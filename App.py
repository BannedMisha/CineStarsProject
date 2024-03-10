"""
    The class App controls most parts of the functionality for the User

    With this App the User can:
        >create an account
        >delete an account
        >Edit account
        >log into the account
        >log out of the account
        >look up the MovieProgram
        >for a specific movie, see how many seats are still available
        >purchase a movie ticket
        >cancel the purchase of a ticket
        >purchase popcorn at the popcorn machine
        >purchase a drink at the popcorn machine
        >rate a movie after (!) viewing it
        >notifications for recent release
        >Search for movies by name/rating/etc.

    Potential future functionality:
        >Link social media account to app
        >Login with social media account (Apple, Google, Twitter, etc.)

    TODO: Graphical Interface
"""

import json
import Tools
import PopcornMachine

loggedIn = False

# In this method the User can create their account
# It takes in the User's details via userinput and attaches them to an instance of the User class
# Also needs to create a password (and account name), probably best to have that be an attribute in the User class
def create_user_account(aID, aAcN, aFiN, aLaN, aBiD, aEma, aPas) -> None:
    file = "saved_classes/user.json"
    inst = {"aID":aID, "aAcN":aAcN, "aFiN":aFiN, "aLaN":aLaN, "aBiD":aBiD, "aEma":aEma, "aPas":aPas}
    cate = "users"

    Tools.write_to_file(file, inst, cate)

# Deletes the Users account
# We secretly keep all the data and sell them to China. Of course.
# TODO: Needs some sort of confirmation before deleting it
def delete_user_account(aID):
    file = "saved_classes/user.json"
    cate = "users"

    Tools.delete_entry_from_file(file, aID, cate)

# Edits the Users account
# TODO: This works for now, but always requires the full info to be added. Better to not require everything each time
def edit_user_account(ID, aAcN, aFiN, aLaN, aBiD, aEma, aPas) -> None:
    file = "saved_classes/user.json"
    inst = {"aAcN": aAcN, "aFiN": aFiN, "aLaN": aLaN, "aBiD": aBiD, "aEma": aEma, "aPas": aPas}
    cate = "users"

    Tools.edit_entry_from_file(file, ID, inst, cate)

# Lets the User log into their account
# To log in the user needs to provide their credentials (account name/email address + password)
def login_account(aAcN, aPas):
    global loggedIn

    file = "saved_classes/user.json"

    with open(file) as jFile:
        data = json.load(jFile)

    for entry in data["users"]:
        if entry.get("aAcN") == aAcN and entry.get("aPas") == aPas:
            loggedIn = True
            print("Login successful")
        else:
            print("Error: Password or Username don't match")


# Logs the User out
# After logging out returns to the main menu of the app
def logout_account():
    global loggedIn

    if loggedIn == True:
        loggedIn = False
        print("You successfully logged out")
    else:
        print("huh?")

# Prints out the complete movie program
# Takes the list from the MovieProgram class and returns it
# ID specifies which movie program we want
def show_program(ID):
    program = Tools.read_from_file("saved_classes/movie_program.json","moviePrograms", ID, "aMoL")
    print(program)

# Shows available seats of a specific movie
# Not sure if Theater also needs to be imported. Probably best to have that be an attribute of MovieProgram?
# TODO: MovieProgram needs to be restructured first to show available seats at specific times
def show_availability():
    pass

# Lets the User buy a ticket
# Also checks if the user's age is appropriate for the movie they want to buy a ticket for
# TODO: Save their bought tickets somewhere externally?
# TODO: MovieProgram needs to be restructured first to show available seats at specific times
def buy_ticket(movie):
    pass

# Lets the User cancel the ticket
# Should print out a list of all bought tickets, user then can pick one and cancel it
# TODO: Save their bought tickets somewhere externally?
# TODO: MovieProgram needs to be restructured first to show available seats at specific times
def cancel_ticket(ticketList):
    pass

# Lets the user see the popcorn menu
def show_popcorn(ID):
    popcorn = Tools.read_from_file("saved_classes/popcorn_machine.json",
                                   "popcornMachines",ID,"aPoM")
    print(popcorn)

# Lets the user see the drinks menu
def show_drinks(ID):
    drinks = Tools.read_from_file("saved_classes/popcorn_machine.json",
                                   "popcornMachines",ID,"aDrM")
    print(drinks)

# Lets the User buy popcorn at the Popcorn Machine™
# Has a console UI for now
# First presents user with a list of the popcorn menu
# Then user can pick one item from the list
# The Popcorn Machine™ creates the popcorn and opens the tray, then closes it after a set time (in PopcornMachine)
def buy_popcorn(ID):
    popcornList = Tools.read_from_file("saved_classes/popcorn_machine.json",
                                   "popcornMachines",ID,"aPoM")

    for index,item in enumerate(popcornList):
        print(f"{index}:{item}")

    uInput = input("Pick your item: ")

    print(f"You picked: {uInput}")
    PopcornMachine.prepare_popcorn()


# Same as buy_popcorn() just with drinks
# Can choose between a few different drinks and sizes
def buy_drink(ID):
    drinkList = Tools.read_from_file("saved_classes/popcorn_machine.json",
                                       "popcornMachines", ID, "aDrM")

    for index, item in enumerate(drinkList):
        print(f"{index}:{item}")

    uInput = input("Pick your item: ")

    print(f"You picked: {uInput}")
    PopcornMachine.prepare_drinks()

# After a movie has been watched, the User receives a notification to rate the movie
# User can rate the movie from 1 to 5 stars
def rate_movie(movie):
    pass

# Lets User create a wishlist of the movies they want to see in the future
# Users can decide if they want to be notified if a movie on their wishlist releases soon. Simple checkmark.
# TODO: Saved externally
def create_wishlist():
    pass

# Notifies the User if a movie on their wishlist is about to release
def notify_wishlist():
    pass

# Lets User search for movies from the movie program
# There should be several different criteria for what to search for
# As Movie has several attributes we can let it search for those. Easy.
# Searching algorithms are fun?
def search_movie(movieProgram):
    pass