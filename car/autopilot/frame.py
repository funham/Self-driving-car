import cv2

from dataclasses import dataclass
from drivetrain.telemetry import Telemetry


@dataclass(frozen=True)
class FrameMeta:
    img: cv2.Mat
    detections: dict
    telemetry: Telemetry
