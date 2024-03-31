from pyfirmata import Arduino, util

port = 'COM4'
board = Arduino(port, baudrate=9600)
iterator = util.Iterator(board)
iterator.start()

led_pin = board.get_pin('d:13:o')
relay_pin = board.get_pin('d:4:o')
electric_fan = board.get_pin('d:7:o')


def control(total):
    
    if total == 0:
        led_pin.write(1)
    elif total == 1:
        led_pin.write(0)
    elif total == 2:
        electric_fan.write(1)
    elif total == 3:
        electric_fan.write(0)
    elif total == 4:
        relay_pin.write(1)
    elif total == 5:
        relay_pin.write(0)
    else:
        print("Invalid")