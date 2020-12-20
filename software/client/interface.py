#!/usr/bin/python3

#Use Pillow for image processing
#Use pyinstaller to bundle application
#/usr/local is the default install location for apps

#For scene config there needs to be defaults in case values are missing

import client

import kivy
import json

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout

# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
# from kivy.uix.widget import Widget
# from kivy.properties import ObjectProperty

class MainMenu(Screen):
    pass

class SelectMenu(Screen):
    pass

class SceneMenu(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class HomeScreen(FloatLayout):
    def client_btn():
        pass
    def scene_button():
        pass
    def logs_btn():
        pass
    def power_btn():
        pass

class Scene():
    pass

class SceneButton():
    pass


kv = Builder.load_file("./kv/pideck.kv")

class PiDeckApp(App):

    def build(self):
        return kv

def other(self):
    pass

if __name__ == '__main__':
    PiDeckApp().run()