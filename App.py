# The class App controls most parts of the functionality for the User
# With this App the User can:
#               >create an account
#               >delete an account
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

    # Copies the attributes of the class User (formerly Kunden) as a new User in the app
    # TODO: Use userID here or in the User class?
    def create_account(self,appUser):
        print()

    # Deletes the users account
    # We secretly keep all the data and sell them to China. Of course.
    def delete_account(self,appUser):
        print()

    # Prints out the complete movie program
    # Takes the list from the MovieProgram class and returns it
    def show_program(self,movieList):
        print()

    # Shows available seats of a specific movie
    # Takes MovieProgram as input
    def show_availability(self,movieProgram):
        print()

    # Lets the User buy a ticket
    # TODO: Maybe needs a new class to have tickets reserved? Maybe in class Theater (formerly Saal)?
    def buy_ticket(self,movie):
        print()

    # Lets the User cancel the ticket
    # Should print out a list of all bought tickets, user then can pick one and cancel it
    def cancel_ticket(self,ticketList):
        print()

    # Lets the User buy popcorn at the Popcorn Machine™
    # Can choose between different sizes and either sweet or salty flavor (or a mix for the adventurous)
    # When the User buys popcorn, he receives a number. If their number is called they can go to the Popcorn Machine™
    # and take pick up their order.
    def buy_popcorn(self):
        print()

    # Same as with buy_popcorn() just with drinks
    # Can choose between three different drinks
    def buy_drink(self):
        print()

    # After a movie has been watched, the User receives a notification to rate the movie
    # User can rate the movie from 1 to 5 stars
    def rate_movie(self):
        print()
