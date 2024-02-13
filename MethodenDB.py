import json
class App:

    appUser = ""

    def __init__(self,appU, title, release_date):
        self.appUser = appU
        self.title = title
        self.release_date = release_date
        self.wishlist = []
        self.watched_movies = []

    def rate_movie(self, movie, rating):
        if movie in self.watched_movies:
            print(f"Du hast {movie.title} bereits bewertet.")
        else:
            # Hier könnte die Logik zur Bewertung des Films implementiert werden
            # Zum Beispiel: movie.rating = rating
            print(f"Du hast {movie.title} mit {rating} Sternen bewertet.")
            self.watched_movies.append(movie)

    def create_wishlist(self, movies, filename="wishlist.json"):
        self.wishlist = movies
        wishlist_data = [{"title": movie.title, "release_date": movie.release_date} for movie in self.wishlist]

        with open(filename, 'w') as file:
            json.dump(wishlist_data, file, indent=2)

    def notify_wishlist(self):
        for movie in self.wishlist:
            if movie not in self.watched_movies:
                print(f"Benachrichtigung: {movie.title} ist verfügbar! Schau ihn dir an.")

    def search_movie(self, title):
        for movie in self.wishlist:
            if movie.title.lower() == title.lower():
                return movie
        print(f"Film mit dem Titel {title} nicht gefunden.")
        return None        
