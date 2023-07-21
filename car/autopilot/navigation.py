from dataclasses import dataclass
from abc import ABC, abstractmethod


class Map:
    @dataclass(frozen=True)
    class Coordinates:
        x: float
        y: float

    def __init__(self):
        ...


class MapLoader(ABC):
    @abstractmethod
    def load(self) -> Map:
        ...


class MapPoint:
    def __init__(self, map: Map, coords: Map.Coordinates):
        ...


class Route:
    def __init__(self, pt_start: MapPoint, pt_end: MapPoint):
        ...
