#!/usr/bin/python3

#Use Pillow for image processing
#Use pyinstaller to bundle application
#/usr/local is the default install location for apps

#For scene config there needs to be defaults in case values are missing

import client

import kivy
import json
import os
from subprocess import call
from multiprocessing import Process

# from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty

from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

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

  dialog = None

  def build(self):
    sm = ScreenManager()
    sm.add_widget(MainMenu(name='main'))
    sm.add_widget(SelectMenu(name='select'))
    sm.add_widget(SceneMenu(name='scene'))

    return sm

  def start_client(self):
    pi_client = client.Client()
    pi_client.start_client()

  def start_scene(self, *args):
    # try:
      # pi_client = client.Client()
      # pi_client.start_client()

    print("starting Socketio Client as process...")
    global client_process
    client_process = Process(target=self.start_client) # assign Flask to a process
    client_process.daemon = True
    client_process.start()  #launch Flask as separate process

    # except Exception as inst:
    #   #Dialog box here
    #   print(inst)
    # else:
    #   print("Client Started")

  def poweroff(self, *args):
    call("sudo nohup shutdown -h now", shell=True)

  def restart(self, *args):
    os.execv(sys.argv[0], sys.argv)

  def show_alert_dialog(self):
    if not self.dialog:
      self.dialog = MDDialog(
        text="Are you sure you want to shutdown?",
        buttons=[
          MDFlatButton(
            text="CANCEL", text_color=self.theme_cls.primary_color, always_release=True
          ),
          MDFlatButton(
            text="SHUTDOWN", text_color=self.theme_cls.primary_color, on_release=self.poweroff()
          ),
        ],
      )
    self.dialog.open()


def other(self):
    pass

if __name__ == '__main__':
    PiDeckApp().run()