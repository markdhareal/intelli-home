import time
from pyfirmata import Arduino, util

# Define the port where your Arduino is connected
port = 'COM4'

# Establish a connection to the Arduino
board = Arduino(port, baudrate=9600)

# Iterate over the digital pins on the board to avoid errors
it = util.Iterator(board)
it.start()

# Define the pin mode
led_pin = board.get_pin('d:13:o')  # Digital pin 13, output mode

# Blink the LED
while True:
    print("LED turned ON")
    led_pin.write(1)  # Turn the LED on
    time.sleep(1)  # Wait for 1 second
    print("LED turned OFF")
    led_pin.write(0)  # Turn the LED off
    time.sleep(1)  # Wait for 1 second
