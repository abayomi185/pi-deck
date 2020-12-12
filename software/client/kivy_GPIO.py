#!/usr/bin/env python

# kivy_GPIO.py
# 2016-11-12
# Public Domain

# sudo apt-get install python-kivy python3-kivy

from kivy.app import App
from kivy.clock import Clock
from kivy.event import EventDispatcher
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.togglebutton import ToggleButton

import pigpio

INPUT=0
OUTPUT=1
SERVO=2
PWM=3

ACTIVE='down'
INACTIVE='normal'

# configure these values

# [GPIO, type] INPUT/OUTPUT/SERVO/PWM

# Input
# [GPIO, INPUT]

# Output, value defaults to 0
# [GPIO, OUTPUT <, value >]

# Servo, value defaults to 1500, min to 1000, max to 2000
# [GPIO, SERVO <, value <, min <, max > > >]

# PWM, value defaults to 0, min to 0, max to 255
# [GPIO, PWM <, value <, min <, max > > >]

CONFIG = [
   [2, SERVO, 0, 1000, 2000],
   [3, SERVO],
   [3, INPUT],
   [4, INPUT],
   [5, OUTPUT, 0],
   [6, PWM, 0],
   [6, INPUT],
   [12, SERVO, 0, 1000, 2000],
   [13, SERVO],
   [14, INPUT],
   [15, OUTPUT, 1],
   [16, PWM, 128],
   [22, SERVO, 1500, 1000, 2000],
   [23, SERVO],
   [24, INPUT],
   [25, OUTPUT, 1],
   [26, PWM, 0,32,190],
]

CONFIG_COLUMNS=2

CONFIG_DEBUG=False # Set to True to enable diagnostics

# end of configuration

widgets = []

class GPIO_Widgets(BoxLayout):

   def set_Servo(self, val):
      val = int(val)
      self.value.text = str(val)
      if self.toggle.state == ACTIVE:
         pi.set_servo_pulsewidth(self.g, val)
         if CONFIG_DEBUG:
            print(self.g, "Servo", val)

   def set_PWM(self, val):
      val = int(val)
      self.value.text = str(val)
      if self.toggle.state == ACTIVE:
         pi.set_PWM_dutycycle(self.g, val)
         if CONFIG_DEBUG:
            print(self.g, "PWM", val)

   def set_Output(self, val):
      val = 1 if val else 0
      self.value.text = "High" if val else "Low"
      pi.write(self.g, val)
      if CONFIG_DEBUG:
         print(self.g, "Output", val)

   def __init__(self, G):

      super(GPIO_Widgets, self).__init__()
      self.cols = 2

      self.g = G[0]
      self.t = G[1]

      label = " " + str(self.g)
      vstr = "Off"

      self.label = Label(text_size=self.size, halign='left', valign='middle',
                     size_hint_x=None, width=100)
      self.add_widget(self.label)

      self.value = Label(text_size=self.size, halign='left', valign='middle',
                     text="Off", size_hint_x=None, width=40)
      self.add_widget(self.value)

      if G[1] == INPUT:

         label += " In"

      elif G[1] == OUTPUT:

         label += " Out"

         value = 0 if len(G) < 3 else G[2]
         v = ACTIVE if value else INACTIVE

         self.toggle = ToggleButton(state=v, size_hint_x=None, width=20)
         self.toggle.text = "" if v == ACTIVE else "0"
         self.toggle.bind(state=self.cb_toggle)
         self.add_widget(self.toggle)

         self.set_Output(value)

      elif G[1] == SERVO:

         label += " Servo"

         value = 1500 if len(G) <  3 else G[2]
         v = ACTIVE if value else INACTIVE

         min   = 1000 if len(G) <  4 else G[3]
         max   = 2000 if len(G) <  5 else G[4]

         self.toggle = ToggleButton(state=v, size_hint_x=None, width=20)
         self.toggle.text = "" if v == ACTIVE else "0"
         self.toggle.bind(state=self.cb_toggle)
         self.add_widget(self.toggle)

         self.slider = Slider(min=min, max=max, value=value)
         self.slider.bind(value=self.cb_slider)
         self.add_widget(self.slider)

         self.set_Servo(self.slider.value)

      elif G[1] == PWM:

         label += " PWM"

         value =   0 if len(G) <  3 else G[2]
         v = ACTIVE if value else INACTIVE

         min   =   0 if len(G) <  4 else G[3]
         max   = 255 if len(G) <  5 else G[4]

         self.toggle = ToggleButton(state=v, size_hint_x=None, width=20)
         self.toggle.text = "" if v == ACTIVE else "0"
         self.toggle.bind(state=self.cb_toggle)
         self.add_widget(self.toggle)

         self.slider = Slider(min=min, max=max, value=value)
         self.slider.bind(value=self.cb_slider)
         self.add_widget(self.slider)

         self.set_PWM(self.slider.value)

      self.label.text = label

   def cb_slider(self, obj, val):
      if self.t == SERVO:
         self.set_Servo(val)
      else:
         self.set_PWM(val)

   def cb_toggle(self, obj, state):

      if state == ACTIVE: # On

         self.toggle.text = ""

         if self.t == SERVO:
            self.set_Servo(self.slider.value)
         elif self.t == PWM:
            self.set_PWM(self.slider.value)
         elif self.t == OUTPUT:
            self.set_Output(1)

      else: # Off

         self.toggle.text = "0"

         if self.t == SERVO:
            pi.set_servo_pulsewidth(self.g, 0)
            if CONFIG_DEBUG:
               print(self.g, "Servo Off")
         elif self.t == PWM:
            pi.set_PWM_dutycycle(self.g, 0)
            if CONFIG_DEBUG:
               print(self.g, "PWM Off")

         elif self.t == OUTPUT:
            self.set_Output(0)

class GPIO_Screen(GridLayout):

   def __init__(self, **kwargs):
      global widgets
      super(GPIO_Screen, self).__init__(**kwargs)
      self.cols = CONFIG_COLUMNS
      self.levels = None

      for G in CONFIG:
         object = GPIO_Widgets(G)
         widgets.append(object)
         self.add_widget(object)

   def update(self, dt):
      levels = pi.read_bank_1()
      if levels != self.levels:
         self.levels = levels
         for s in widgets:
            if s.t == INPUT:
               v = "High" if levels & (1<<s.g) else "Low"
               s.value.text = v

class GPIO_App(App):

   title = "Pi GPIO"

   def build(self):
      app = GPIO_Screen()
      Clock.schedule_interval(app.update, 0.1)
      return app

import pigpio

pi = pigpio.pi()

if not pi.connected:
   exit()

try:
   GPIO_App().run()
except KeyboardInterrupt:
   pass

print("exiting")

for G in CONFIG:

   if G[1] == SERVO:
      pi.set_servo_pulsewidth(G[0], 0)

   elif G[1] == PWM:
      pi.set_PWM_dutycycle(G[0], 0)

pi.stop()

