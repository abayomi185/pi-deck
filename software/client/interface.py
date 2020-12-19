#!/usr/bin/python3

import client

import kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget

# class HomeScreen(GridLayout):

#     def __init__(self, **kwargs):
#         super(HomeScreen, self).__init__(**kwargs)

#         self.cols = 1

#         self.inside = GridLayout()
#         self.inside.cols = 2

#         self.inside.add_widget(Label(text='User Name'))
#         self.inside.username = TextInput(multiline=False)
#         self.inside.add_widget(self.inside.username)

#         self.add_widget(self.inside)

#         self.start = Button(text="Submit", font_size=40)
#         self.start.bind(on_press=self.pressed)
#         self.add_widget(self.start)

#     def pressed(self, instance):
#         print("pressed")

class HomeScreen(Widget):
    pass

class PiDeckApp(App):

    def build(self):
        return HomeScreen()


if __name__ == '__main__':
    PiDeckApp().run()