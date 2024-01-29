
class Movie: # Blauplan
    # Klassenattribut
    mRating = "To be announced"
    mLength = "To be announced"
    mGenre = "To be announced"
    mPrice = "To be announced"
    mReleaseDate = "To be announced"
    mAgeRating = "To be announced"
    mDescription = "To be announced"

    # Objektattributen
    def __init__(self, mID, mName, mRating, mLength, mGenre, mPrice, mReleaseDate, mAgeRating, mDescription):
        self.mID = mID
        self.mName = mName
        self.mRating = mRating
        self.mLength = mLength
        self.mGenre = mGenre
        self.mPrice = mPrice
        self.mReleaseDate = mReleaseDate
        self.mAgeRating = mAgeRating
        self.mDescription = mDescription

    def get_all_info(self): # Methode: Film Infos Abrufen
        print("Movie ID: " + str(self.mID) + "\nName: "+ self.mName + "\nRating: " + str(self.mRating) + "\nMovie Length: " + str(self.mLength) + "\nGenre: " + self.mGenre + "\nMovie Price: " + str(self.mPrice) + "\nRelease Date: " + str(self.mReleaseDate) + "\nAge Rating: " + str(self.mAgeRating) + "\nDescription: " + self.mDescription)

    # wird mit movie Programm interagieren
    def add_movie_to_movieList(self): # Methode: Film ID in der Liste hinzufugen
        if self.mID not in MovieList.listOfMovies:
            MovieList.append(self.mID)

    # wird mit kunden_alter interagieren
    def is_allowed_for_underage(self): # Methode: Prüfen ob Kunde den Ticket kaufen kann
        if self.mAgeRating > Kunden.altaer:
            print("Age restriction")

    # Wird ins App erzeugt, frag mich nicht wie
    def get_notif_when_release(self): # Methode: Notif wann der Film veröffentlicht wird
        pass

    # das gehört vllt zu app, oder?
    def search_by_name(self): # Methode: Film suchen
        if self.mName in MovieList:
            print("Tickets für" + self.mName + "sind verfügbar")

    # wird entweder mit Saal interagieren
    def show_screen(self): # Methode: Film Saal abrufen
        pass

# Objekt wird erzeugt, Konstruktoraufruf

Kill_Bill = Movie(1, "Kill Bill Vol1", 8.1, 111, "Action", 12, 2003-10-10, 15, "It stars Uma Thurman as the Bride,"
                                                                               " a former assassin who swears revenge on a group of assassins")
Kill_Bill.get_all_info()
