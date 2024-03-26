import json
import Tools
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

# Global variables to track login status
loggedIn = False
logged_user = ""


class WelcomeScreen(Screen):
    pass


class LogInScreen(Screen):
    """
    This function checks if the username matches the password. It also changes to status of loggedIn to true and
    keeps track of the logged_user.
    """
    def login_account(self):
        aAcN = self.ids.user.text
        aPas = self.ids.password.text
        global loggedIn
        global logged_user

        file = "saved_classes/user.json"

        with open(file) as jFile:
            data = json.load(jFile)

        for entry in data["users"]:
            if entry.get("aAcN") == aAcN and entry.get("aPas") == aPas:
                loggedIn = True
                logged_user = aAcN
                pop = Popup(title='Congrats',
                            content=Label(text='Login successful!.'),
                            size_hint=(None, None), size=(200, 100))
                pop.open()
                self.manager.current = 'fourth'
                break
        else:
            pop = Popup(title='Error',
                        content=Label(text='Username and password do not match!'),
                        size_hint=(None, None), size=(300, 100))
            pop.open()

    """
    This functions tackles any attempts to logging in without completing all the forms. When all the field are filled
    the user can proceed to the menu. 
    """

    def submit(self):
        if (self.ids.welcome_login.text == "" or
                self.ids.user.text == ""):
            pop = Popup(title='Invalid Form',
                        content=Label(text='Please complete all the fields.'),
                        size_hint=(None, None), size=(250, 100))
            pop.open()
        else:
            self.login_account()
            self.clear()


    """
    This function clears the username and password fields
    """
    def clear(self):
        self.ids.user.text = ""
        self.ids.password.text = ""


class CreateAccountScreen(Screen):
    """
    Function that creates a new account instance using the user's input.
    Traces the logged_user and sets the status of logged_in to True. The new account is saved in the User JSON file.
    """

    def create_user_account(self):
        global logged_user
        global loggedIn
        aID = self.ids.id_person.text
        aAcN = self.ids.person.text
        aFiN = self.ids.Firstname.text
        aLaN = self.ids.Lastname.text
        aBiD = self.ids.bday.text
        aEma = self.ids.email.text
        aPas = self.ids.pas1.text

        file = "saved_classes/user.json"
        inst = {"aID": aID, "aAcN": aAcN, "aFiN": aFiN, "aLaN": aLaN, "aBiD": aBiD, "aEma": aEma, "aPas": aPas}
        cate = "users"
        logged_user = aAcN
        loggedIn = True
        Tools.write_to_file(file, inst, cate)

    """
    Simple functions the clears on the fields
    """

    def clear(self):
        self.ids.id_person.text = ""
        self.ids.person.text = ""
        self.ids.Firstname.text = ""
        self.ids.Lastname.text = ""
        self.ids.bday.text = ""
        self.ids.email.text = ""
        self.ids.pas1.text = ""

    """ 
    Similar  to the other one, this functions tackles any attempts to creating an account
    without completing all the forms. If the forms are left not completed a pop-up will appear and the user won't be 
    able to proceed. When the all the fields are completed a pop-up confirmation will appear.
    """

    def submit(self):
        if (self.ids.id_person.text == "" or
                self.ids.person.text == "" or
                self.ids.Firstname.text == "" or
                self.ids.Lastname.text == "" or
                self.ids.bday.text == "" or
                self.ids.email.text == "" or
                self.ids.pas1.text == ""):
            pop = Popup(title='Invalid Form',
                        content=Label(text='Please complete all the fields.'),
                        size_hint=(None, None), size=(250, 100))
            pop.open()
        else:
            self.create_user_account()
            self.clear()
            pop = Popup(title='Congrats',
                        content=Label(text='Account successfully created!.'),
                        size_hint=(None, None), size=(250, 100))
            pop.open()
            self.manager.current = 'fourth'


class MenuScreen(Screen):
    """
    Function that changes the status of global variables loggedIn. When called the user will the logged out and the
    logged_user instance will be cleared.
    """

    def logout_account(self):
        global loggedIn
        global logged_user
        if loggedIn is True:
            loggedIn = False
            logged_user = ""
            pop = Popup(title='Bye',
                        content=Label(text='You have successfully logged out'),
                        size_hint=(None, None), size=(300, 100))
            pop.open()
        else:
            pop = Popup(title='Error',
                        content=Label(text='Something went wrong!'),
                        size_hint=(None, None), size=(300, 100))
            pop.open()


class MyAccount(Screen):
    """
    This function changes the hint text in the fill in text forms using the information from the User JSON file.
    """

    def change_hint_text(self):
        global logged_user
        self.ids.user_id.hint_text = Tools.read_from_file_mod("saved_classes/user.json", "users", logged_user, "aID")
        self.ids.user_user.hint_text = Tools.read_from_file_mod("saved_classes/user.json", "users", logged_user, "aAcN")
        self.ids.f_name.hint_text = Tools.read_from_file_mod("saved_classes/user.json", "users", logged_user, "aFiN")
        self.ids.l_name.hint_text = Tools.read_from_file_mod("saved_classes/user.json", "users", logged_user, "aLaN")
        self.ids.b_day.hint_text = Tools.read_from_file_mod("saved_classes/user.json", "users", logged_user, "aBiD")
        self.ids.eml.hint_text = Tools.read_from_file_mod("saved_classes/user.json", "users", logged_user, "aEma")
        self.ids.passs.hint_text = Tools.read_from_file_mod("saved_classes/user.json", "users", logged_user, "aPas")

    def edit_user_info(self):
        """
        This function tracks the instance of the logged user, and edits the user's account information based on the
        entered information. If in the text fields wasn't entered any information the attribute values will remain
        unchanged.
        """
        global logged_user
        file = "saved_classes/user.json"

        instance = {"aID": self.ids.user_id.text,
                    "aAcN": self.ids.user_user.text,
                    "aFiN": self.ids.f_name.text,
                    "aLaN": self.ids.l_name.text,
                    "aBiD": self.ids.b_day.text,
                    "aEma": self.ids.eml.text,
                    "aPas": self.ids.passs.text}
        category = "users"
        ID = logged_user
        Tools.edit_entry_from_file_modified(file, ID, instance, category)


class ListingsScreen(Screen):
    pass


class FoodScreen(Screen):
    pass


class WishlistScreen(Screen):
    # class MovieTile(BoxLayout):  # save the attributes as paths
    #     image_source = StringProperty("")
    #     title = StringProperty("")
    #     genre = StringProperty("")
    #     length = StringProperty("")
    #     Rating = StringProperty("")
    #
    #     def __init__(self, movie_id, **kwargs):
    #         super(MovieTile, self).__init__(**kwargs)
    #         self.movie_id = movie_id
    #         self.movie_title = Tools.read_from_file("movie.json", "movies", id, "aNam")
    #         self.movie_genre = Tools.read_from_file("movie.json", "movies", id, "aGen")
    #         self.movie_length = Tools.read_from_file("movie.json", "movies", id, "aLen")
    #         self.movie_rating = Tools.read_from_file("movie.json", "movies", id, "aStr")
    pass



class OrdersScreen(Screen):
    pass


class DeleteAccountScreen(Screen):
    def delete_user_account(self):
        """
        This function tracks the instance of the logged user, and making it able for the logged user to delete only
        his/her account information. If the user is logged in we can successfully delete the account. If not a pop-up
        error will be shown.
        """
        global logged_user

        aAcN = self.ids.user_to_del.text
        file = "saved_classes/user.json"  # note to self: THIS NEEDS TO BE RENAMED ACCORDINGLY !!!
        cate = "users"
        if logged_user == aAcN:
            Tools.delete_entry_from_file_mod(file, aAcN, cate)
            pop = Popup(title='Bummer',
                        content=Label(text='Account successfully deleted!'),
                        size_hint=(None, None), size=(300, 100))
            pop.open()
        else:
            pop = Popup(title='Nah Uh',
                        content=Label(text='Please enter the correct id!'),
                        size_hint=(None, None), size=(300, 100))
            pop.open()


class BuyTicket(Screen, Widget):
    def spinner_week(self, value):
        self.ids.label_week.text = f"You selected: {value}"

    def spinner_day(self, value):
        self.ids.label_day.text = f"You selected: {value}"

    def spinner_movie(self, value):
        self.ids.label_movie.text = f"You selected: {value}"




    def buy_choice(self):
        thisWeek =self.ids.spinner_week.text
        day = self.ids.spinner_day.text
        movieID = self.ids.spinner_movie.text

        result = Tools.ticket_buyer(thisWeek,day,movieID)

        if result is True:
            pop = Popup(title='Congratulations!',
                        content=Label(text='Your ticket has been purchased!'),
                        size_hint=(None, None), size=(300, 100))
            pop.open()
        else:
            pop = Popup(title='Oops!',
                        content=Label(text='There was an error purchasing your ticket.'),
                        size_hint=(None, None), size=(300, 100))
            pop.open()


class WindowManager(ScreenManager):
    pass


# Loading all the kv files
Builder.load_file("GUI Structure and resources/welcome.kv")
Builder.load_file("GUI Structure and resources/logIn.kv")
Builder.load_file("GUI Structure and resources/createAccount.kv")
Builder.load_file("GUI Structure and resources/Menu.kv")
Builder.load_file("GUI Structure and resources/changeAccount.kv")
Builder.load_file("GUI Structure and resources/Cinema_listing.kv")
Builder.load_file("GUI Structure and resources/food_menu.kv")
Builder.load_file("GUI Structure and resources/wishlist.kv")
Builder.load_file("GUI Structure and resources/my_orders.kv")
Builder.load_file("GUI Structure and resources/delete_account.kv")
Builder.load_file("GUI Structure and resources/buy_ticket.kv")


class MainApp(MDApp):
    """
    This is the main app module, serves more functions, such as setting the primary app color palette and managing
    all the app's screens
    """
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        screen_manager = WindowManager()
        screen_manager.add_widget(WelcomeScreen(name="first"))
        screen_manager.add_widget(LogInScreen(name="second"))
        screen_manager.add_widget(CreateAccountScreen(name="third"))
        screen_manager.add_widget(MenuScreen(name="fourth"))
        screen_manager.add_widget(MyAccount(name="fifth"))
        screen_manager.add_widget(ListingsScreen(name="sixth"))
        screen_manager.add_widget(FoodScreen(name="seventh"))
        screen_manager.add_widget(WishlistScreen(name="eighth"))
        screen_manager.add_widget(OrdersScreen(name="ninth"))
        screen_manager.add_widget(DeleteAccountScreen(name="tenth"))
        screen_manager.add_widget(BuyTicket(name="eleven"))
        return screen_manager


if __name__ == "__main__":
    MainApp().run()
