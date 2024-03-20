"""
    This class handles the attributes of movies
"""

class Movie:
    aID          = ""
    aName        = ""
    aLength      = 0
    aGenre       = ""
    aPrice       = 0.01                 # TODO: In MovieProgram?
    aReleaseDate = ""
    aAgeRating   = 0
    aStarRating  = 0.1
    a2DPossible  = False
    a3DPossible  = False
    aDescription = "To be announced"    # TODO: Save externally?


    def __init__(self,aID,aNam,aLen,aGen,aPri,aReD,aAgR,aStR,a2D,a3D,aDes):
        self.aID          = aID
        self.aName        = aNam
        self.aLength      = aLen
        self.aGenre       = aGen
        self.aPrice       = aPri
        self.aReleaseDate = aReD
        self.aAgeRating   = aAgR
        self.aStarRating  = aStR
        self.a2DPossible  = a2D
        self.a3DPossible  = a3D
        self.aDescription = aDes


    # Getter/Setter Methods
    def set_move_info(self):
        pass

    def get_movie_info(self):
        pass