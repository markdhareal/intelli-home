from pyfirmata import Arduino, util

class ArduinoConfig:
    def __init__(self):
        self.board = Arduino('COM4')
        self.iterator = util.Iterator(self.board)
        self.iterator.start()

    def get_pin(self, arduino_pin):
        return self.board.get_pin(arduino_pin)
    
    def set_pin_mode(self, pin_mode, mode):
        pin_mode.mode = mode

    def digital_write(self, pin, value):
        pin.write(value)