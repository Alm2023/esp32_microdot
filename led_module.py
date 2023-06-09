from machine import Pin

class LEDModule:
    """This will represent our LED"""
    
    def __init__(self, pinNumber):
        self.pinNumber = pinNumber
        self.led_pin = Pin(self.pinNumber, Pin.OUT)
        
    def get_value(self):
        return self.led_pin.value()
    
    def get_pinNumber(self):
        return self.pinNumber

    def on(self):
        self.led_pin.value(1)

    def off(self):
        self.led_pin.value(0)
    

    def toggle(self):
        self.led_pin.value(not self.get_value())
    