"""
    This module handles the graphical user interface
"""

import json
import tool_user
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivymd.uix.behaviors import HoverBehavior


#has_account = False this was needed for the OG logger but we might change the function and
#instead move this into the welcome window where the user has to choose if he logs in or creates an account

# class HoverItem(HoverBehavior):
#     def on_enter(self, *args):
#
#         self.md_bg_color = (1, 1, 1, 1)
#
#     def on_leave(self, *args):
#
#         self.md_bg_color = self.theme_cls.bg_darkest

class WelcomeScreen(Screen):
    pass

class LogInScreen(Screen):
    pass

class CreateAccountScreen(Screen):
    pass

class MenuScreen(Screen):
    pass

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
        return screen_manager

    def logger(self): # this is the log in function that I previously created,
        # it needs to be linked with the logIn.kv
        # if the log in is successful this will lead to another window

        pass

    def clear(self): # this just deletes the input if the user so chooses
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""


if __name__ == "__main__":
    MainApp().run()

