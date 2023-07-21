from dataclasses import dataclass
from parking_sensor import ParkingSensors
from distance_tracker import DistanceTracker


@dataclass(frozen=True)
class TelemetryData:
    parking_sensors: tuple
    distance_travelled: float


class Telemetry:
    def __init__(self, distance_tracker: DistanceTracker, parking_sensors: ParkingSensors):
        self.distansce_tracker = distance_tracker
        self.parking_sensors = parking_sensors

    def update(self) -> TelemetryData:
        park_sensors_data = self.parking_sensors.update()
        distance_travelled = self.distansce_tracker.update()
