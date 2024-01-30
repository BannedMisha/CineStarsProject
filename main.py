"""
Python 2 Group Project: CineStars

CineStars is a concept for a fully automated cinema including a companion phone App to access tickets and more.
"""

# I copied the whole main method from another code I made before. It sucks. Good enough for now.

import os

import App


# To clear console
def cls():
    os.system('clear')


# To end a command
def cmnd():
    print("")
    input("Press any key to continue ...")
    cls()


# Starts the game
def start():

    print("===============================================================")
    print("CineStars App")
    print()
    print("1. Show Movie Program")
    print("2. Buy Ticket")
    print("3. Delete Account")
    print("===============================================================")
    print("")
    userInput = input("What do you want to do? ")



# When main gets initialized, clears console
if __name__ == '__main__':
    cls()
    start()