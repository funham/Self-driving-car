import RPi.GPIO as GPIO
import cfg


class ParkingSensorUnit:
    def __init__(self, pin):
        self._pin = pin
        GPIO.setup(self._pin, GPIO.IN)

    def is_triggered(self) -> bool:
        return GPIO.input(self._pin)


class ParkingSensors:
    def __init__(self, *pinout) -> None:
        assert len(pinout) == cfg.N_PARKING_SENSORS
        self.units = (ParkingSensorUnit(pin) for pin in pinout)

    def update(self) -> tuple:
        return tuple(unit.is_triggered() for unit in self.units)
