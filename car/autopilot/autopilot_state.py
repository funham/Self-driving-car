from abc import ABC, abstractmethod
from autopilot import Autopilot
from frame import FrameMeta
from singleton import Singleton


class AutopilotState(ABC, metaclass=Singleton):
    @abstractmethod
    def enter_state(self, ap: Autopilot) -> None:
        pass

    @abstractmethod
    def exit_state(self, ap: Autopilot) -> None:
        pass

    @abstractmethod
    def feed(self, ap: Autopilot, frame_meta: FrameMeta) -> None:
        """Uses detections information and camera view to determine car's behaviour"""
        pass
