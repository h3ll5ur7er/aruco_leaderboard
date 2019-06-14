from enum import IntEnum
import gpiozero
from .framework import Singleton

class GpioController(metaclass=Singleton):
    LED_PIN = 18 # pwm pin
    def __init__(self):
        self._led = gpiozero.PWMLED(pin=self.LED_PIN, initial_value=0)
        self._led_state = 0
    def set_led(self, value):
        if value>1:
            value = 1
        if value<0:
            value = 0
        self._led.value
