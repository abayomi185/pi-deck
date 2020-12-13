import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time

class Buttons():

  def __init__(self, user_pins):    
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BCM) # Use physical pin numbering
    
    self.pins = user_pins
    # print(self.pins)
    self.init_pins()

  def init_pins(self):
    for x in range(0, len(self.pins)):
      GPIO.setup(self.pins[x], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
      GPIO.add_event_detect(self.pins[x], GPIO.RISING, callback=self.btn_callback, 
                                  bouncetime=200)

  def btn_callback(self, channel):
    print('button pressed {}'.format(channel))

def main():
  pins = [26, 16, 12, 25, 24, 23]
  b = Buttons(pins)
  input("Press enter to exit ;)")

if __name__ == "__main__":
  main()