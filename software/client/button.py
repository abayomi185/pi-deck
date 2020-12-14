import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time

class Pin():
  
  def __init__(self, pin_number):
      self.pin = pin_number
      self.is_active = False
  

class Buttons():

  def __init__(self, user_pins):    
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BCM) # Use physical pin numbering
    
    self.pins = user_pins
    # print(self.pins)
    # self.callback = callback_func
    self.init_pins()

  def init_pins(self):
    for x in range(0, len(self.pins)):
      GPIO.setup(self.pins[x], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
      # GPIO.add_event_detect(self.pins[x], GPIO.RISING, callback=send_input_to_client, 
      #                             bouncetime=200)

  def set_pin_callback(self, callback_func):
    for x in range(0, len(self.pins)):
      GPIO.add_event_detect(self.pins[x], GPIO.RISING, callback=callback_func, 
                                  bouncetime=200)

def send_input_to_client(channel):
    print('button pressed {}'.format(channel))
    client.send_input_key_event(channel)

def main():
  pins = [26, 16, 12, 25, 24, 23]
  b = Buttons(pins)
  input("Press enter to exit ;)")

if __name__ == "__main__":
  main()