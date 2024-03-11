import json
import Tools
import PopcornMachine
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.label import Label

loggedIn = False

class WelcomeScreen(Screen):
    pass

class LogInScreen(Screen):
    # this needs to be debugged ASAP- yeah it works noooooow biiiiiiitch
    def login_account(self):
        aAcN = self.ids.user.text
        aPas = self.ids.password.text
        global loggedIn

        file = "user.json"

        with open(file) as jFile:
            data = json.load(jFile)

        for entry in data["users"]:
            if entry.get("aAcN") == aAcN and entry.get("aPas") == aPas:
                loggedIn = True
                pop = Popup(title='Congrats',
                            content=Label(text='Login successful!.'),
                            size_hint=(None, None), size=(200, 100))
                pop.open()
                break
        else:
            pop = Popup(title='Error',
                        content=Label(text='Username and password do not match!'),
                        size_hint=(None, None), size=(300, 100))
            pop.open()


    def clear(self): # this just deletes the input if the user so chooses
        self.ids.user.text = ""
        self.ids.password.text = ""
class CreateAccountScreen(Screen):


    def create_user_account(self):
        aID = self.ids.id_person.text
        aAcN = self.ids.person.text
        aFiN = self.ids.Firstname.text
        aLaN = self.ids.Lastname.text
        aBiD = self.ids.bday.text
        aEma = self.ids.email.text
        aPas = self.ids.pas1.text

        file = "user.json"
        inst = {"aID": aID, "aAcN": aAcN, "aFiN": aFiN, "aLaN": aLaN, "aBiD": aBiD, "aEma": aEma, "aPas": aPas}
        cate = "users"

        Tools.write_to_file(file, inst, cate)

    def clear(self):  # this just deletes the input if the user so chooses
        self.ids.id_person.text = ""
        self.ids.person.text = ""
        self.ids.Firstname.text = ""
        self.ids.Lastname.text = ""
        self.ids.bday.text = ""
        self.ids.email.text = ""
        self.ids.pas1.text = ""

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
    def logout_account(self):
        global loggedIn

        if loggedIn is True:
            loggedIn = False
            pop = Popup(title='Bye',
                        content=Label(text='You have successfully logged out'),
                        size_hint=(None, None), size=(300, 100))
            pop.open()
        else:
            pop = Popup(title='Error',
                        content=Label(text='Something went wrong!'),
                        size_hint=(None, None), size=(300, 100))
            pop.open()

#HOW DO I INSTANTIATE THE ACCOUNT THAT NEEDS TO BE DELETED
class MyAccount(Screen):
    pass

class ListingsScreen(Screen):
    pass

class FoodScreen(Screen):
    pass

class WishlistScreen(Screen):
    pass

class OrdersScreen(Screen):
    pass

class DeleteAccountScreen(Screen):
    def delete_user_account(self):
        aID = self.ids.user_to_del.text
        file = "user.json"  # note to self: THIS NEEDS TO BE RENAMED ACCORDINGLY !!!
        cate = "users"
        pop = Popup(title='Bummer',
                    content=Label(text='Account successfully deleted!'),
                    size_hint=(None, None), size=(300, 100))
        pop.open()
        Tools.delete_entry_from_file(file, aID, cate)
class WindowManager(ScreenManager):
    pass


Builder.load_file("welcome.kv")
Builder.load_file("logIn.kv")
Builder.load_file("createAccount.kv")
Builder.load_file("Menu.kv")
Builder.load_file("changeAccount.kv")
Builder.load_file("Cinema_listing.kv")
Builder.load_file("food_menu.kv")
Builder.load_file("wishlist.kv")
Builder.load_file("my_orders.kv")
Builder.load_file("delete_account.kv")
class MainApp(MDApp):
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
        return screen_manager



if __name__ == "__main__":
    MainApp().run()

