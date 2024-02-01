"""
    The class App controls most parts of the functionality for the User

    TODO: Does this even need to be a class?
    With this App the User can:
        >create an account
        >delete an account
        >Edit account
        >log into the account
        >log out of the account
        >look up the MovieProgram
        >for a specific movie, see how many seats are still available
        >purchase a movie ticket
        >cancel the purchase of a ticket
        >purchase popcorn at the popcorn machine
        >purchase a drink at the popcorn machine
        >rate a movie after (!) viewing it
        >notifications for recent release
        >Search for movies by name/rating/etc.

        Potential future functionality:
        >Link social media account to app
        >Login with social media account (Apple, Google, Twitter, etc.)
"""

class App:

    appUser = "placeholder"

    def __init__(self,appU):
        self.appUser = appU

    # In this method the User can create their account
    # It takes in the User's details via userinput and attaches them to an instance of the User class (formerly Kunden)
    # Also needs to create a password (and account name), probably best to have that be an attribute in the User class
    def create_account(self,appUser):
        pass

    # Deletes the Users account
    # We secretly keep all the data and sell them to China. Of course.
    def delete_account(self,appUser):
        pass

    # Edits the Users account
    def edit_account(self,appUser):
        pass

    # Lets the User log into their account
    # To log in the user needs to provide their credentials (account name/email address + password)
    def login_account(self,appUser):
        pass

    # Logs the User out
    # After logging out returns to the main menu of the app
    def logout_account(self,appUser):
        pass

    # Prints out the complete movie program
    # Takes the list from the MovieProgram class and returns it
    def show_program(self,movieProgram):
        pass

    # Shows available seats of a specific movie
    # Takes MovieProgram as input
    # Not sure if Theater also needs to be imported. Probably best to have that be an attribute of MovieProgram?
    def show_availability(self,movieProgram):
        pass

    # Lets the User buy a ticket
    # Also checks if the user's age is appropriate for the movie they want to buy a ticket for
    # TODO: Save their bought tickets somewhere externally?
    def buy_ticket(self,movie):
        pass

    # Lets the User cancel the ticket
    # Should print out a list of all bought tickets, user then can pick one and cancel it
    # TODO: Save their bought tickets somewhere externally?
    def cancel_ticket(self,ticketList):
        pass

    # Lets the User buy popcorn at the Popcorn Machine™
    # Can choose between different sizes and either sweet or salty flavor (or a mix for the adventurous)
    # When the User buys popcorn, he receives a number. If their number is called they can go to the Popcorn Machine™
    # and take pick up their order.
    def buy_popcorn(self):
        pass

    # Same as buy_popcorn() just with drinks
    # Can choose between a few different drinks and sizes
    def buy_drink(self):
        pass

    # After a movie has been watched, the User receives a notification to rate the movie
    # User can rate the movie from 1 to 5 stars
    def rate_movie(self, movie):
        pass

    # Lets User create a wishlist of the movies they want to see in the future
    # Users can decide if they want to be notified if a movie on their wishlist releases soon. Simple checkmark.
    # TODO: Saved externally
    def create_wishlist(self):
        pass

    # Notifies the User if a movie on their wishlist is about to release
    def notify_wishlist(self):
        pass

    # Lets User search for movies from the movie program
    # There should be several different criteria for what to search for
    # As Movie has several attributes we can let it search for those. Easy.
    # Searching algorithms are fun?
    def search_movie(self,movieProgram):
        pass