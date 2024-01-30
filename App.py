# The class App controls most parts of the functionality for the User
# With this App the User can:
#               >create an account
#               >delete an account
#               >log into the account
#               >log out of the account
#               >look up the MovieProgram
#               >for a specific movie, see how many seats are still available
#               >purchase a movie ticket
#               >cancel the purchase of a ticket
#               >purchase popcorn at the popcorn machine
#               >purchase a drink at the popcorn machine
#               >rate a movie after (!) viewing it

class App:

    appUser = "placeholder"

    def __init__(self,appU):
        self.appUser = appU

    # In this method the user can create their account
    # It takes in the user's details via userinput and attaches them to an instance of the User class (formerly Kunden)
    # Also needs to create a password (and account name), probably best to have that be an attribute in the User class
    # TODO: User class needs to be finished first to create this method
    def create_account(self,appUser):
        pass

    # Deletes the users account
    # We secretly keep all the data and sell them to China. Of course.
    def delete_account(self,appUser):
        pass

    # Lets the user log into their account
    # To log in the user needs to provide their credentials (account name/email address + password)
    def login_account(self,appUser):
        pass

    # Logs the user out
    # After logging out returns to the main menu of the app
    def logout_account(self,appUser):
        pass

    # Prints out the complete movie program
    # Takes the list from the MovieProgram class and returns it
    # TODO: Need to see the MovieProgram class first to add functional code
    def show_program(self,movieProgram):
        pass

    # Shows available seats of a specific movie
    # Takes MovieProgram as input
    # Not sure if Theater also needs to be imported. Probably best to have that be an attribute of MovieProgram?
    def show_availability(self,movieProgram):
        pass

    # Lets the User buy a ticket
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
    # TODO: Needs a functional PopPopcorn class first
    def buy_popcorn(self):
        pass

    # Same as with buy_popcorn() just with drinks
    # Can choose between a few different drinks and sizes
    # TODO: Needs a functional PopDrink class first
    def buy_drink(self):
        pass

    # After a movie has been watched, the User receives a notification to rate the movie
    # User can rate the movie from 1 to 5 stars
    def rate_movie(self, movie):
        pass
