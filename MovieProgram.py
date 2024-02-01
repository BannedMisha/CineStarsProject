"""
    This class handles the move program
"""

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