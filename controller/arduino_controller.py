from pyfirmata import Arduino, util

port = 'COM8'
board = Arduino(port, baudrate=9600)
iterator = util.Iterator(board)
iterator.start()

led_pin = board.get_pin('d:4:o')
relay_pin = board.get_pin('d:7:o')
electric_fan = board.get_pin('d:8:o')

# Initialize pin states
led_state = 0
electric_fan_state = 0
relay_pin_state = 0

def control(total):
    global led_state, electric_fan_state, relay_pin_state
    
    # Handling for each total value
    if total == 0:
        led_state = 1
    elif total == 1:
        led_state = 0
    elif total == 2:
        electric_fan_state = 1
    elif total == 3:
        electric_fan_state = 0
    elif total == 4:
        relay_pin_state = 1
    elif total == 5:
        relay_pin_state = 0
    else:
        print("Invalid")

    # Write the pin states
    led_pin.write(led_state)
    electric_fan.write(electric_fan_state)
    relay_pin.write(relay_pin_state)
