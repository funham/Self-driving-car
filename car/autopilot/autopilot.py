import cv2

from autopilot_state import AutopilotState
from drivetrain.drivetrain import Drivetrain
from frame import FrameMeta


class Autopilot:
    def __init__(self, drivetrain: Drivetrain, initial_state: AutopilotState):
        self.drivetrain = drivetrain
        self.state = initial_state

    def change_state(self, new_state: AutopilotState) -> None:
        """Should only be called from DrivingState.feed()"""
        self.state.exit_state(self)
        self.state = new_state
        self.state.enter_state(self)

    def feed(self, frame) -> None:
        self.state.feed(self, frame)
