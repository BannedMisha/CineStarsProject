"""
    This module handles several useful functions that are needed in other modules

    It's the backbone of the whole program
"""

import json


"""
========================================================================================================================

    This block handles everything that interacts with JSON files
    > Add entry to a file
    > Read contents from a file
    > Read multiple contents from a file as a list
    > Read multiple contents from a file as a dictionary
    > Delete an entry from a file
    > Edit the whole entry of a file
    > Edit one item of a entry of a file

========================================================================================================================
"""
# -----------------------------------------------------------------------------
# THESE ARE THE FUNCTIONS I PREVIOUSLY MODIFIED AB HIER
# -----------------------------------------------------------------------------

# I know now we have convert_id_to_name and vice versa, but I'll leave it like this for now
def read_from_file_mod(file, category, username, item):
    with open(file) as jFile:
        data = json.load(jFile)

    for user in data.get(category, []):
        if user.get("aAcN") == username:
            if item in ['aAcN', 'aFiN', 'aLaN', 'aBiD', 'aEma']:
                value = user.get(item)
                print(f"Found value: {value}")
                return value if value is not None else ""
            else:
                print("Item not found in allowed list")
                return ""
    print("Username not found")
    return ""


def delete_entry_from_file_mod(file, ID, category):
    with open(file) as jFile:
        data = json.load(jFile)

    for entry in data[category]:
        if entry.get('aAcN') == ID:
            for key in entry.keys():
                if key != 'aAcN':
                    entry[key] = None

    with open(file, 'w') as wFile:
        json.dump(data, wFile, indent=4)


# I think this was deleted? I'm still using it though
def write_to_file(file, instance, category) -> None:
    with open(file) as jFile:
        data = json.load(jFile)

    data[category].append(instance)

    with open(file, 'w') as wFile:
        json.dump(data, wFile, indent=4)

# Function to save a classes attributes to their corresponding JSON file
# file     : the name of the file (E.g. "saved_classes/movie_program.json")
# instance : The contents of the things we add (see AdminApp.create_movie() as example)
# category : the category (E.g. "moviePrograms")
def add_entry_to_file(file, instance, category) -> None:
        with open(file) as jFile:
            data = json.load(jFile)

        data[category].append(instance)

        with open(file, 'w') as wFile:
            json.dump(data, wFile, indent=4)


# Function to return the value of a specific entry of a JSON file
# file     : the name of the file (E.g. "saved_classes/movie_program.json")
# category : the category (E.g. "moviePrograms")
# ID       : the ID of the specific class instance we want the content from (E.g. "MP0002")
# item     : the item we are looking for (E.g. "aMoL")
def read_from_file(file, category, ID, item):
    with open(file) as jFile:
        data = json.load(jFile)

    for content in data.get(category):
        if content['aID'] == ID:
            return content.get(item)


# Similar to the previous function read_from_file() this function returns the content from multiple items based on
# their item name category thing
# file     : the name of the file (E.g. "saved_classes/movie_program.json")
# category : the category (E.g. "moviePrograms")
# item     : the item we are looking for (E.g. "aMoL")
def read_multiple_from_file(file, category, item) -> list:
    with open(file) as jFile:
        data = json.load(jFile)

    contentList = []
    for entry in data[category]:
        content = entry.get(item)
        if content:
            contentList.append(content)

    return contentList


# Returns all keys and values from an entry
# file     : the name of the file (E.g. "saved_classes/movie_program.json")
# category : the category (E.g. "moviePrograms")
# ID       : the ID of the specific class instance we want the content from (E.g. "MP0002")
def read_full_from_file(file, category, ID) -> dict:
    with open(file) as jFile:
        data = json.load(jFile)

    contentDict = {}
    for entry in data.get(category,[]):
        if entry["aID"] == ID:
            contentDict[ID] = entry
            break

    return contentDict


# With this function you can delete an entry from a JSON file
# This will not completely delete it, aIDs will remain unique and one-use only, but it will scrub the information
# file     : the name of the file (E.g. "saved_classes/movie_program.json")
# category : the category (E.g. "moviePrograms")
# ID       : the ID of the specific class instance we want the content from (E.g. "MP0002")
def delete_entry_from_file(file, category, ID) -> None:
    with open(file) as jFile:
        data = json.load(jFile)

    for entry in data[category]:
        if entry.get('aID') == ID:
            for key in entry.keys():
                if key != 'aID':
                    entry[key] = None

    with open(file, 'w') as wFile:
        json.dump(data, wFile, indent=4)


# With this function you can edit the whole entry from a JSON file
# file     : the name of the file (E.g. "saved_classes/movie_program.json")
# instance : The contents of the things we edit (see AdminApp.create_movie() as example)
# category : the category (E.g. "moviePrograms")
# ID       : the ID of the specific class instance we want the content from (E.g. "MP0002")
def edit_entry_from_file(file, instance, category, ID) -> None:
    with open(file) as jFile:
        data = json.load(jFile)

    for entry in data[category]:
        if entry.get('aID') == ID:
            for key, value in instance.items():
                if key != 'aID':
                    entry[key] = value

    with open(file, 'w') as wFile:
        json.dump(data, wFile, indent=4)

# With this function you can edit a specific item of an entry in a JSON file
# file     : the name of the file (E.g. "saved_classes/movie_program.json")
# category : the category (E.g. "moviePrograms")
# ID       : the ID of the specific class instance we want the content from (E.g. "MP0002")
# item     : the item we are editing (E.g. "aMoL")
# change   : the value that entry is changed to
def edit_item_from_file(file, category, ID, item, change) -> None:
    with open(file) as jFile:
        data = json.load(jFile)

    for content in data.get(category):
        if content['aID'] == ID:
            if type(change) == type(content[item]):
                content[item] = change
            else:
                print("Error: Mismatched data type. File has not been edited.")

    with open(file, 'w') as wFile:
        json.dump(data, wFile, indent=4)

"""
========================================================================================================================

    This block contains a few useful tools that are needed in some functions
    > Convert an ID to a name
    > Convert a name to an ID
    > Check for duplicates within a JSON file
    > Generate an ID for when a new entry for a JSON file is created

========================================================================================================================
"""

# This function returns the name for a specific object from its ID
# file     : the name of the file (E.g. "saved_classes/movie_program.json")
# category : the category (E.g. "moviePrograms")
# ID       : the ID of the specific class instance we want the content from (E.g. "MP0002")
def convert_id_to_name(file, category, ID) -> str:
    with open(file, 'r') as jFile:
        data = json.load(jFile)

    for entry in data[category]:
        if entry["aID"] == ID:
            return entry.get("aNam", "Error: No 'aNam' entry found for the given ID.")


# This function returns the id for a specific object from its name
# file     : the name of the file (E.g. "saved_classes/movie_program.json")
# category : the category (E.g. "moviePrograms")
# name       : the name of the specific class instance we want the content from (E.g. "Jimmy")
def convert_name_to_id(file, category, name) -> str:
    with open(file, 'r') as jFile:
        data = json.load(jFile)

    for entry in data[category]:
        if entry["aNam"] == name:
            return entry.get("aID", "Error: No 'aNam' entry found for the given ID.")

# This function checks for duplicates in JSON files
# Returns False if there's no duplicate and True if there is a duplicate already
# file     : the name of the file (E.g. "saved_classes/movie_program.json")
# category : the category (E.g. "moviePrograms")
# item     : the item we are trying to compare (e.g. "aNam")
# comp     : the thing we want to check for duplicates
def duplicate_checker(file, category, item, comp) -> bool:
    with open(file, 'r') as jFile:
        data = json.load(jFile)
        listItems = [entry[item].lower() for entry in data[category]]
        comp_lower = comp.lower()
        if comp_lower in listItems:
            print(f"{comp} (case-insensitive) already exists in {item} category.")
            return True
        else:
            print(f"{comp} (case-insensitive) does not exist in {item} category.")
            return False

# This function creates IDs
# file     : the name of the file (E.g. "saved_classes/movie_program.json")
# ident    : the identifier that precedes the ID (e.g. Movie identifier is M0001)
def id_generator(file, ident) -> str:
    with open(file, 'r') as jFile:
        data = json.load(jFile)
        usedIDs = [int(movie['aID'][1:]) for movie in data['movies']]
        nextID = max(usedIDs) + 1 if usedIDs else 1
        return f"{ident}{nextID:04d}"



"""
========================================================================================================================

    This block contains major functionality for the functions in AdminApp.py
    > Alters the JSON file for the movie program, also adds the correct number of open seats to each movie

========================================================================================================================
"""

# This function populates a movie program with their seats
# Takes the max Capacity, theater ID and program (True Curr week, False next week) of a theater as input
# Then it saves it to theater_seats.json, names are converted to IDs
def populate_movie_seats(idTheater, thisWeek):
    movieList = show_movie_list(idTheater, thisWeek)
    program = {}
    maxCap = read_from_file("saved_classes/theater.json", "theaters", idTheater, "aMax")

    movieListID = list(map(lambda x: convert_name_to_id("saved_classes/movie.json","movies",x)
                           , movieList))

    for day in ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]:
        program[day] = {}
        for movie in movieListID:
            program[day][movie] = maxCap

    if thisWeek:
        saveLocation = "saved_classes/theater_seats_current.json"
    else:
        saveLocation = "saved_classes/theater_seats_next.json"

    with open(saveLocation, "w") as jFile:
        json.dump(program, jFile, indent=4)



"""
========================================================================================================================

    This block contains major functionality for the functions in App.py
    > Buys a ticket, returns True if a ticket has successfully been bought
    > Saves a bought ticket to the JSON file (NYI)
    > Display movie program as a list
    > Display movie program as a dictionary including available seats

========================================================================================================================
"""

# This function has the actual functionality of buying a ticket
# thisWeek : boolean, True for current week, False for next week
# day      : string, name of the day (e.g. "WED")
# movieID  : string, ID of the movie the user wants to buy the ticket of
# Returns True if a ticket has been successfully bought
def ticket_buyer(thisWeek, day, movieID) -> bool:
    ticketBought = False

    if thisWeek:
        fileLocation = "saved_classes/theater_seats_current.json"
    else:
        fileLocation = "saved_classes/theater_seats_next.json"

    with open(fileLocation, "r") as jFile:
        movieProgram = json.load(jFile)

    if day in movieProgram and movieID in movieProgram[day]:
        if movieProgram[day][movieID] > 0:
            movieProgram[day][movieID] -= 1
            ticketBought = True
        else:
            print("Error: No more available seats")

        with open(fileLocation, "w") as jFile:
            json.dump(movieProgram,jFile, indent=4)

    return ticketBought

# Saves the ticket that has been bought to a json file
# userID   : the ID of the user
# movieID  : the ID of the movie that the ticket has been bought for
# thisWeek : boolean, True for current week, False for next week
# day      : which day the movie was bought
# this should be automatically activate when App.buy_ticket() returns True
def ticket_saver(userID, movieID, thisWeek, day):

    pass

# This function displays a list of all the movies that are being aired in a theater
# id_theater : the ID of the theater we want to see the movie list of
def show_movie_list(idTheater, thisWeek) -> list:
    file = "saved_classes/theater.json"
    category = "theaters"
    fileCon = "saved_classes/movie.json"
    categoryCon = "movies"

    if thisWeek:
        program = read_from_file(file, category, idTheater, "aPCW")
    else:
        program = read_from_file(file, category, idTheater, "aPNW")

    convertedProgram = list(map(lambda x: convert_id_to_name(fileCon, categoryCon, x), program))

    return convertedProgram

# This function returns the movie program for a specific week
# thisWeek : boolean, True for current week, False for next week
def show_full_program(thisWeek) -> dict:
    if thisWeek:
        fileLocation = "saved_classes/theater_seats_current.json"
    else:
        fileLocation = "saved_classes/theater_seats_next.json"

    with open(fileLocation, "r") as jFile:
        movieProgram = json.load(jFile)

    return movieProgram