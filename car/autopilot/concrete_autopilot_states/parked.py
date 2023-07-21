from autopilot.autopilot_state import Autopilot, AutopilotState
from frame import FrameMeta


class Parked(AutopilotState):
    def enter_state(self, ap: Autopilot) -> None:
        # TODO beep-beep & shut down (probably new state is needed)
        ap.drivetrain.disable()

    def exit_state(self, ap: Autopilot) -> None:
        # TODO beep-beep & start up (probably new state is needed)
        ap.drivetrain.engage()

    def feed(self, ap: Autopilot, frame_meta: FrameMeta) -> None:
        pass  # being IDLE while parked
