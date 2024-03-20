"""
Python 2 Group Project: CineStars

CineStars is a concept for a fully automated cinema including a companion phone App to access tickets and more.
"""

import os

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
    file = "saved_classes/movie.json"
    ident = "M"
    category = "movies"
    item = "aNam"
    name = "armageddon"
    ID   = "M0001"

    test = "you didn't even use a function bruh"    # DEBUG

    #test = Tools.id_generator(file, ident)
    #test = Tools.duplicate_checker(file, category, item, name)
    #test = Tools.read_multiple_from_file(file, category, item)
    #test = Tools.read_from_file(file, category, ID, item)
    #test = Tools.read_full_from_file(file, category, ID)
    #test = Tools.show_movie_list("T0001")
    #test = Tools.populate_movie_seats(30, "T0001", True)
    #test = Tools.show_full_program(True)
    #test = Tools.ticket_buyer(True,"TUE","M0003")

    #test2 = App.buy_ticket(True, "FRI", "M0001")

    print(test)

    pass


# When main gets initialized, clears console
if __name__ == '__main__':
    cls()
    test_function_to_test_stuff()
    #start()