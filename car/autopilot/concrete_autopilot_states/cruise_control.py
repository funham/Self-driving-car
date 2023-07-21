from autopilot.autopilot_state import Autopilot, AutopilotState
from frame import FrameMeta


class CruiseControl(AutopilotState):
    def enter_state(self, ap: Autopilot) -> None:
        pass

    def exit_state(self, ap: Autopilot) -> None:
        pass

    def feed(self, ap: Autopilot, frame_meta: FrameMeta) -> None:
        ...
