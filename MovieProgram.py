"""
    This class handles the move program
"""

# TODO: Does this even need to be a class? There is only one movie program at a time?
#       If we would have more than one cinema it would make sense so implement it as a class anyway, I guess.

class MovieProgram:
    aCinema    = ""    # If we keep it as a class, this specifies which cinema this program is for. Make class Cinema?
    aMovieList = []

    def __init__(self,aCin,aMoL):
        self.aCinema    = aCin
        self.aMovieList = aMoL

    # Getter/Setter Methods
    def set_program_info(self):
        pass

    def get_program_info(self):
        pass

    # Adds a movie to a list or rather changes the program itself
    # TODO: Doesn't feel right to put it in here, but it's definitely not part of App.
    #       New class to handle organisation stuff?
    def change_movie_program(self):
        pass