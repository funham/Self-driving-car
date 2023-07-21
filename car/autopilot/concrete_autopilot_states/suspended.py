from autopilot.autopilot_state import Autopilot, AutopilotState
from frame import FrameMeta


class Suspended(AutopilotState):
    def enter_state(self, ap: Autopilot) -> None:
        ap.drivetrain.gear.set_speed(0)

    def exit_state(self, ap: Autopilot) -> None:
        pass

    def feed(self, ap: Autopilot, frame_meta: FrameMeta) -> None:
        ...  # awaiting untill there's a way to go
