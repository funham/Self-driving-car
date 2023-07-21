import RPi.GPIO as GPIO
from utils import sign, clip


class Servo:
    MAX_SPEED = 200

    def __init__(self, pin):
        self._pin = pin

        GPIO.setup(self._pin, GPIO.OUT)
        self._pwm = GPIO.PWM(self._pin, 50)
        self._pwm.start(0)
        self._angle = 0
        self._speed = 0

    def set_angle(self, t_angle: float) -> None:
        self.t_angle = t_angle

    def update(self, dt: float) -> float:
        assert 0 <= self.t_angle <= 180

        if abs(self._angle - self.t_angle) < 1:
            self._angle = self.t_angle
            self._speed = 0
            self._pwm.ChangeDutyCycle(0)

        else:
            err = self.t_angle - self._angle
            self._angle += clip(self._speed * dt, -abs(err), abs(err))

            err = self.t_angle - self._angle

            duty = self.t_angle / 18 + 2
            self._pwm.ChangeDutyCycle(duty)

            self._speed = sign(err) * Servo.MAX_SPEED

        return self._angle


if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)

    servo = Servo(pin=3)

    while True:
        servo.update(12, 0.1)
