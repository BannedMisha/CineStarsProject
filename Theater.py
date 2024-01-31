"""
PSEUDOCODE

Klasse Saal:
    Initialisierung saalName, saalCapacity, saalType
        saalName = saalName
        saalCapacity = saalCapacity
        saalType = saalType

# Beispiele für Filme
movie1 = Movie("The Transporter", 18, 120, "Action")
movie2 = Movie("Inception", 12, 150, "Sci-Fi")
movie3 = Movie("The Shawshank Redemption", 16, 142, "Drama")
movie4 = Movie("The Dark Knight", 14, 152, "Action")
movie5 = Movie("Forrest Gump", 12, 142, "Drama")

# Beispiele für Säle
saal1 = Saal("Saal 1", 100, "Standard")
saal2 = Saal("Saal 2", 50, "VIP")
saal3 = Saal("Saal 3", 200, "3D")

# Bibliothek erstellen
library = MovieLibrary()

# Filme zur Bibliothek hinzufügen
library.add_movie(movie1)
library.add_movie(movie2)
library.add_movie(movie3)
library.add_movie(movie4)
library.add_movie(movie5)

# Filme anzeigen
library.display_movies()

"""





class Theater:

    seatMatrix = [[],           # Shows a matrix of available seats in a theater
                  [],
                  []]

    def __init__(self, seatM):
        self.seatMatrix = seatM