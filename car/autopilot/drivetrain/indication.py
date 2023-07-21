import RPi.GPIO as GPIO
from enum import Enum
from monotonic_timer import Timer
from utils import LRPair


class LED:
    class Power(Enum):
        OFF = GPIO.LOW
        ON = GPIO.HIGH

    def __init__(self, pin) -> None:
        self._pin = pin
        self._state = LED.Power.OFF
        self._is_blinking = False
        self._blinking_period = None
        self._timer = Timer()

        GPIO.setup(self._pin, GPIO.OUT)
        GPIO.output(self._pin, GPIO.LOW)

    def toggle(self, state: Power) -> None:
        self._state = state
        GPIO.output(self.s_pin, self._state)

    @property
    def state(self) -> bool:
        return self._state

    def set_blinking(self, period: float) -> None:
        self._is_blinking = True
        self._blinking_period = period

    def stop_blinking(self) -> None:
        self._is_blinking = False

    def update(self) -> None:
        if not self._is_blinking:
            return

        if not self._timer.is_expired():
            return

        self._timer.set(self._blinking_period)

        if self._state == LED.Power.OFF:
            self.toggle(LED.Power.ON)
        elif self._state == LED.Power.OFF:
            self.toggle(LED.Power.ON)


class LEDLRPair(LRPair):
    def __init__(self, left: LED, right: LED):
        super().__init__(left, right)

    def toggle(self, state: LED.Power) -> None:
        self.left.toggle(state)
        self.right.toggle(state)

    @property
    def state(self) -> tuple[bool]:
        return self.left.state, self.right.state

    def set_blinking(self, period: float) -> None:
        self.left.set_blinking(period)
        self.right.set_blinking(period)

    def stop_blinking(self) -> None:
        self.left.stop_blinking()
        self.right.stop_blinking()

    def update(self) -> None:
        self.left.update()
        self.right.update()


class Klaxon:
    def __init__(self, pin) -> None:
        self._pin = pin

        GPIO.setup(self._pin, GPIO.OUT)
        self._pwm = GPIO.PWM(self._pin, 50)
        self._pwm.ChangeDutyCycle(0)

    def push(self) -> None:
        self._pwm.ChangeDutyCycle(13)

    def release(self) -> None:
        self._pwm.ChangeDutyCycle(0)


class Indication:
    def __init__(self, stop_signal_pin, reverse_signal_pin, l_blinker_pin, r_blinker_pin, klaxon_pin) -> None:
        self.stop_lights = LED(stop_signal_pin)
        self.reverse_lights = LED(reverse_signal_pin)
        self.blinkers = LEDLRPair(LED(l_blinker_pin), LED(r_blinker_pin))
        self.klaxon = Klaxon(klaxon_pin)

    def update(self) -> None:
        self.reverse_lights.update()
        self.stop_lights.update()
        self.blinkers.update()
