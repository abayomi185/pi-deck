import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time

def button_callback(channel):
    print("Button was pushed!")
    # time.sleep(0.4)

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

GPIO.add_event_detect(23, GPIO.RISING, callback=button_callback, bouncetime=200) # Setup event on pin 10 rising edge

message = input("Press enter to quit\n\n") # Run until someone presses enter

GPIO.cleanup() # Clean up

