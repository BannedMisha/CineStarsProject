"""
    This class handles the attributes of movies
"""

class Movie:
    aName        = ""
    aLength      = 0
    aGenre       = ""
    aPrice       = 0.01                 # TODO: In MovieProgram?
    aReleaseDate = ""
    aAgeRating   = 0
    aStarRating  = 0
    a2DPossible  = False
    a3DPossible  = False
    aDescription = "To be announced"    # TODO: Save externally?


    def __init__(self,mNam,mLen,mGen,mPri,mReD,mAgR,mStR,a2D,a3D,mDes):
        self.aName        = mNam
        self.aLength      = mLen
        self.aGenre       = mGen
        self.aPrice       = mPri
        self.aReleaseDate = mReD
        self.aAgeRating   = mAgR
        self.aStarRating  = mStR
        self.a2DPossible  = a2D
        self.a3DPossible  = a3D
        self.aDescription = mDes


    # Getter/Setter Methods
    def set_move_info(self):
        pass

    def get_movie_info(self):
        pass