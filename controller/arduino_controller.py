from pyfirmata import Arduino, util

port = 'COM8'
board = Arduino(port, baudrate=9600)
iterator = util.Iterator(board)
iterator.start()

led_pin = board.get_pin('d:4:o')
relay_pin = board.get_pin('d:7:o')

led_pin_state = 0
relay_pin_state = 0

def control(total):
    global led_pin_state, relay_pin_state

    if total == 0:
        led_pin_state = 1
    elif total == 1:
        led_pin_state = 0
    elif total == 2:
        relay_pin_state = 0
    elif total == 3:
        relay_pin_state = 1
    elif total == 4:
        led_pin_state = 0
        relay_pin_state = 1
    elif total == 5:
        led_pin_state = 1
        relay_pin_state = 0


    led_pin.write(led_pin_state)
    relay_pin.write(relay_pin_state)
