# Import all board pins and bus interface.
import board
import busio
import time

# Import the HT16K33 LED matrix module.
from adafruit_ht16k33 import matrix

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Create the matrix class.
# This creates a 16x8 matrix:
# matrix = matrix.Matrix16x8(i2c)
# Or this creates a 8x8 matrix:
#matrix = matrix.Matrix8x8(i2c)
# Or this creates a 8x8 bicolor matrix:
#matrix = matrix.Matrix8x8x2
# Finally you can optionally specify a custom I2C address of the HT16k33 like:
matrix = matrix.Matrix16x8(i2c, address=0x77, auto_write=True, brightness=0.1)

# Clear the matrix.
matrix.fill(1)

# Set a pixel in the origin 0,0 position.

for x in range(3):
    for y in range(3):
        matrix[x, y] = 1
        # matrix.show()
        print("[{}, {}]\n".format(x, y))
        time.sleep(3)

    


# Set a pixel in the middle 8, 4 position.
# matrix[8, 4] = 1
# Set a pixel in the opposite 15, 7 position.
# matrix[15, 7] = 1
# matrix.show()

# Change the brightness
# matrix.brightness = 1

# Set the blink rate
# matrix.blink_rate = 2