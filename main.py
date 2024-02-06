"""
Python 2 Group Project: CineStars

CineStars is a concept for a fully automated cinema including a companion phone App to access tickets and more.
"""

# I copied the whole main method from another code I made before. It sucks. Good enough for now.

import os
import json

import AdminApp
import App
import Cinema as cin


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
def test_function_to_test_stuff(file, aID):
    pass


# When main gets initialized, clears console
if __name__ == '__main__':
    cls()
    #start()
    #test_function_to_test_stuff('saved_classes/cinema.json','C002')