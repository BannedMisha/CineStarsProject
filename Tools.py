"""
    This module handles several useful functions that are needed in other modules
"""


import json

# Function to save a classes attributes to their corresponding JSON file
# Better than to have duplicates of this functionality in each "create"-function
def write_to_file(file, instance, category) -> None:
        with open(file) as jFile:
            data = json.load(jFile)

        data[category].append(instance)

        with open(file, 'w') as wFile:
            json.dump(data, wFile, indent=4)


# Function to return contents from a JSON file
# file     : the name of the file (E.g. "saved_classes/movie_program.json")
# category : the category (E.g. "moviePrograms") TODO: Automate this
# ID       : the ID of the specific class instance we want the content from (E.g. "MP0002")
# item     : the item we are looking for (E.g. "aMoL")
# Returns a list?
def read_from_file(file, category, ID, item):
    with open(file) as jFile:
        data = json.load(jFile)

    for content in data.get(category):
        if content['aID'] == ID:
            return content.get(item)


# Similar to the previous function read_from_file() this function returns the content from multiple items based on
# their item name category thing
def read_multiple_from_file(file, category, item):
    with open(file) as jFile:
        data = json.load(jFile)

    contentList = []
    for entry in data[category]:
        content = entry.get(item)
        if content:
            contentList.append(content)

    return contentList

# With this function you can delete an entry from a json file
# This will not completely delete it, aIDs will remain unique and one-use only, but it will scrub the information
def delete_entry_from_file(file, ID, category):
    with open(file) as jFile:
        data = json.load(jFile)

    for entry in data[category]:
        if entry.get('aID') == ID:
            for key in entry.keys():
                if key != 'aID':
                    entry[key] = None

    with open(file, 'w') as wFile:
        json.dump(data, wFile, indent=4)


def edit_entry_from_file(file, ID, instance, category):
    with open(file) as jFile:
        data = json.load(jFile)

    for entry in data[category]:
        if entry.get('aID') == ID:
            for key, value in instance.items():
                if key != 'aID':
                    entry[key] = value

    with open(file, 'w') as wFile:
        json.dump(data, wFile, indent=4)



# TODO: This doesn't really do anything at the moment???
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


# -----------------------------------------------------------------------------
# THESE ARE THE FUNCTIONS I PREVIOUSLY MODIFIED
# -----------------------------------------------------------------------------

# I know now we have convert_id_to_name and vice versa, but I'll leave it like this for now
def read_from_file_mod(file, category, ID, item):
    with open(file) as jFile:
        data = json.load(jFile)

    for content in data.get(category):
        if content['aAcN'] == ID:
            return content.get(item)

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


def edit_entry_from_file_mod(file, ID, instance, category):
    with open(file) as jFile:
        data = json.load(jFile)

    for entry in data[category]:
        if entry.get('aAcN') == ID:
            for key, value in instance.items():
                if key != 'aAcN':
                    entry[key] = value

    with open(file, 'w') as wFile:
        json.dump(data, wFile, indent=4)

# This fixes a bug

def edit_entry_from_file_modified(file, ID, instance, category):
    with open(file) as jFile:
        data = json.load(jFile)

    for entry in data[category]:
        if entry.get('aAcN') == ID:
            for key, value in instance.items():
                if value:  # Only update if a non-empty value is provided
                    entry[key] = value

    with open(file, 'w') as wFile:
        json.dump(data, wFile, indent=4)
# I think this was deleted? I'm still using it though
def write_to_file(file, instance, category) -> None:
    with open(file) as jFile:
        data = json.load(jFile)

    data[category].append(instance)

    with open(file, 'w') as wFile:
        json.dump(data, wFile, indent=4)


def ticket_buyer(thisWeek, day, movieID) -> bool:
    ticketBought = False

    if thisWeek:
        fileLocation = "saved_classes/theater_seats_current_re.json"
    else:
        fileLocation = "saved_classes/theater_seats_next_re.json"

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
