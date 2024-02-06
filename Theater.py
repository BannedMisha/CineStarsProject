"""
    This class handles the attributes of theaters in our cinema
"""


class Theater:

    aID          = ""
    aName        = ""
    aMaxCapacity = 0
    aCurCapacity = 0
    aSeatMatrix  = [[],           # Shows a matrix of available seats in a theater
                   [],            # It only sounds complicated because it is
                   []]

    def __init__(self, aID, aNam, aMax, aCur, aSeM):
        self.aID          = aID
        self.aName        = aNam
        self.aMaxCapacity = aMax
        self.aCurCapacity = aCur
        self.aSeatMatrix  = aSeM

    # getter/setter methoden benutzt
    def set_theater_info(self):
        pass

    def get_theater_info(self):
        pass

#ich wollte den code hier oben nicht ändern zu Sicherheit *********Also ab hier habe ich gemacht ( Arlind)

class Movie:
    def __init__(self, titel, dauer, genre):
        self.titel = titel
        self.dauer = dauer
        self.genre = genre 

    def __str__(self):
        return f"{self.titel} ({self.dauer} min) - {self.genre}"  #für die Ausgabe 

class MovieProgram:
    def __init__(self):
        self.filme = [] #eine Leere Liste erstellt

    def film_hinzufuegen(self, film):
        self.filme.append(film) #filme zu der Liste hinzufügen

    def programm_anzeigen(self):
        print("Movieprogramm: ")
        for film in self.filme: #hier habe ich eine for schleife benutzt um alle Filme im Programm anzuzeigen
            print(film) #Printet die Filme ein

    def verfuegbarkeit_anzeigen(self):
        print("\nVerfügbare Plätze: ")
        for i, film in enumerate(self.filme, 1):
            freie_plaetze = 50 - len(film.reservierte_plaetze) #berechnet die Anzahl der freien Plätze
            print(f"{i}. {film.titel}: {freie_plaetze} Plätze verfügbar") #


# Beispiel FilmProgramm erstellen
film1 = Movie("Inception", 150, "Sci-Fi")
film1.reservierte_plaetze = set()
film2 = Movie("The Dark Knight", 152, "Action")
film2.reservierte_plaetze = set()
film3 = Movie("Titanic", 195, "Romance")
film3.reservierte_plaetze = set()

programm = MovieProgram()
programm.film_hinzufuegen(film1)
programm.film_hinzufuegen(film2)
programm.film_hinzufuegen(film3)

#*********************
programm.programm_anzeigen()
programm.verfuegbarkeit_anzeigen()

