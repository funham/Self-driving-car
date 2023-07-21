from drivetrain.motor import Motor
from drivetrain.servo import Servo
from drivetrain.indication import Indication
from drivetrain.telemetry import Telemetry, TelemetryData

from ticker import Ticker

import RPi.GPIO as GPIO


class Drivetrain:
    def __init__(self, power_pin: int, motor: Motor, servo: Servo, indication: Indication, telemetry: Telemetry) -> None:
        self.power_pin = power_pin

        self.gear = motor
        self.steering_rack = servo
        self.indication = indication
        self.telemetry = telemetry
        self.telemetry_data = telemetry.update()

        self._engaged = False

        GPIO.setup(power_pin, GPIO.OUT)
        GPIO.output(power_pin, GPIO.LOW)

    def update(self) -> None:
        self.steering_rack.update(Ticker.dt)
        self.indication.update()
        self.telemetry_data = self.telemetry.update()

    def disable(self) -> None:
        self._engaged = False
        GPIO.output(self.power_pin, GPIO.LOW)

    def engage(self) -> None:
        self._engaged = True
        GPIO.output(self.power_pin, GPIO.HIGH)

    def __del__(self) -> None:
        self.disable()
        GPIO.cleanup()
