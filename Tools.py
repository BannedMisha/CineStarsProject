"""
    This module handles several useful functions that are needed in other modules
"""


import json

# Function to save a classes attributes to their corresponding JSON file
# Better than to have duplicates of this functionality in each "create"-function
def write_to_file(file, instance, category) -> None:
    try:
        with open(file) as jFile:
            data = json.load(jFile)

        data[category].append(instance)

        with open(file, 'w') as wFile:
            json.dump(data, wFile, indent=4)

    except FileNotFoundError:
        print("ERROR: File not found")


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