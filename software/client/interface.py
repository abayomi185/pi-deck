#!/usr/bin/python3

#Use Pillow for image processing
#Use pyinstaller to bundle application
#/usr/local is the default install location for apps

#For scene config there needs to be defaults in case values are missing

import client

import kivy
import json

# from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty

# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
from kivy.uix.widget import Widget
# from kivy.properties import ObjectProperty

class MainMenu(Screen):
  text_var = StringProperty()
  text_var = "select label"

class SelectMenu(Screen):
  pass

class SceneMenu(Screen):
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

class Scene(Screen):
  pass

class SceneButton(Widget):
  pass

class SceneSelected():
  pass

kv = Builder.load_file("./kv/pideck.kv")

class PiDeckApp(MDApp):

  text_var1 = StringProperty()
  text_var1 = "select label1"

  text_var2 = StringProperty()
  text_var2 = "select label2"

  color_white = (1, 1, 1, 1)
  color_gray1 = (0.8, 0.8, 0.8, 1)
  color_black = (0, 0, 0, 0)
  color_blue = (0.01, 0.66, 0.96, 1)

  def start_scene(self, *args):
    pi_client = Client()
    pi_client.start_client()
    print("Client Started")

  def build(self):
    sm = ScreenManager()
    sm.add_widget(MainMenu(name='main'))
    sm.add_widget(SelectMenu(name='select'))
    sm.add_widget(SceneMenu(name='scene'))

    return sm

def other(self):
    pass

if __name__ == '__main__':
    PiDeckApp().run()