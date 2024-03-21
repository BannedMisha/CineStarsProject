"""
Python 2 Group Project: CineStars

CineStars is a concept for a fully automated cinema including a companion phone App to access tickets and more.
"""

import os

import AdminApp
import Tools

os.environ['TERM'] = 'xterm'    # This makes an annoying error message no longer appear
                                # I don't know why it be like that, but it do

# To clear console
def cls():
    os.system('clear')


# To end a command
def cmnd():
    print("")
    input("Press any key to continue ...")
    cls()


# Starts the app
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


# Does what you think it would do
def test_function_to_test_stuff():
    test = "you didn't even use a function bruh"    # DEBUG

    Tools.edit_item_from_file("saved_classes/theater.json","theaters", "T0001", "aMax",
                              "dog")

    print(test)

    pass


# When main gets initialized, clears console
if __name__ == '__main__':
    cls()
    test_function_to_test_stuff()
    #start()