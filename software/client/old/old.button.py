import pigpio
import time

pi = pigpio.pi()

class Buttons():

  def __init__(self, user_pins):
    self.pins = user_pins
    # print(self.pins)
    self.init_pins()

  def init_pins(self):
    for x in range(0, len(self.pins)):
      pi.set_mode(self.pins[x], pigpio.INPUT)
      pi.set_pull_up_down(self.pins[x], pigpio.PUD_DOWN)
      # pi.event_callback(self.pins[x], self.btn_callback)
  
  def btn_callback(self):
    print("Button pressed")

def main():
  # pins = [23, 24, 25, 1, 12, 16]
  pins = [23, 24, 25, 26, 12, 16]
  b = Buttons(pins)
  pi.event_callback(23, print("press"))

  input("Press enter to exit ;)")

  # while True:
  #   print(bin(pi.read_bank_1()))
  #   time.sleep(1)

if __name__ == "__main__":
  main()