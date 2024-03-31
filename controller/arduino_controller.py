from pyfirmata import Arduino, util

port = 'COM4'
board = Arduino(port, baudrate=9600)
iterator = util.Iterator(board)
iterator.start()
led_pin = board.get_pin('d:13:o')
relay_pin = board.get_pin('d:4:o')
electric_fan = board.get_pin('d:7:o')

# Variable to keep track of whether 5 has been detected previously
five_detected = False

def control(total):
    global five_detected
    
    if total == 5:
        if not five_detected:
            led_pin.write(1)
            five_detected = True
        else:
            led_pin.write(0)
            five_detected = False
    else:
        if not five_detected:
            led_pin.write(1)
