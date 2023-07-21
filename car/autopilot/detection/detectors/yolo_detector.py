"""
Implementation of Yolo model detectors
"""

import cv2
import yolopy

from detection.detector import IDetector


class YoloV4Detector(IDetector):
    def __init__(self, path):
        self.model = yolopy.Model(
            path, use_uint8=True, use_timvx=True, cls_num=1)

    def forward(self, frame: cv2.Mat) -> dict:
        ...


class YoloV5Detector(IDetector):
    def __init__(self, path):
        self.model = ...

    def forward(self, frame: cv2.Mat) -> dict:
        return {}


class YoloV8Detector(IDetector):
    def __init__(self, path):
        self.model = ...

    def forward(self, frame: cv2.Mat) -> dict:
        ...
        return {}
