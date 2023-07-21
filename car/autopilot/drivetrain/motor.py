import RPi.GPIO as GPIO

from utils import clip
from enum import Enum


class Motor:
    class Direction(Enum):
        FORWARD = 1
        BACKWARD = 0

    MAX_SPEED: int = 75

    def __init__(self, in1: int, in2: int, en: int) -> None:
        GPIO.setup(in1, GPIO.OUT)
        GPIO.setup(in2, GPIO.OUT)
        GPIO.setup(en, GPIO.OUT)

        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)

        self.in1 = in1
        self.in2 = in2
        self._pwm = GPIO.PWM(en, 1000)
        self._pwm.start(25)

        self._speed = 0
        self._suspended = True

    def stop(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)

        self._suspended = True
        self._dir = None
        self._speed = 0

    @property
    def direction(self) -> Direction | None:
        return self._direction

    @direction.setter
    def direction(self, dir: Direction):
        self._direction = dir
        self._suspended = False

        if dir == Motor.Direction.FORWARD:
            GPIO.output(self.in1, GPIO.HIGH)
            GPIO.output(self.in2, GPIO.LOW)

        if dir == Motor.Direction.BACKWARD:
            GPIO.output(self.in1, GPIO.LOW)
            GPIO.output(self.in2, GPIO.HIGH)

        else:
            raise ValueError('You can choose directions from Motor.Direction')

    @property
    def speed(self):
        return self._speed

    def set_speed(self, val: int):
        if self._suspended:
            raise ValueError

        assert val >= 0

        self._speed = clip(val, 0, Motor.MAX_SPEED)
        self._pwm.ChangeDutyCycle(self._speed)


if __name__ == '__main__':
    motor = Motor(24, 23, 25)

    motor.direction = Motor.Direction.FORWARD
    motor.speed = 34
