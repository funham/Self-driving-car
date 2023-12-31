import cfg
import cv2
import numpy as np


class StoplineDetector:
    def __init__(self):
        ...

    def get_stopline_distance(self, layout: cv2.Mat, out_img: cv2.Mat) -> float:
        """Calculates the distance to the nearest crossroad."""
        assert len(layout.shape) == 2

        h, w = layout.shape

        stopline_h, stopline_w = 25, 150

        y0 = int(h - h / 2)

        x1 = (w - stopline_w) // 2
        x2 = x1 + stopline_w

        # vertical histogram of a layout
        hist = layout[y0:, w//2:x2].sum(axis=1)
        # index of a brightest row in on the layout, supposedly a crossroad.
        maxi = hist.argmax()

        # if the brightest row is not bright enough to be a crossroad then no crossroad detected
        if hist[maxi] / 255 < 60:
            return np.inf, (0, 0), (0, 0)

        y1 = maxi + y0 - stopline_h // 2
        y2 = y1 + stopline_h

        cv2.rectangle(out_img, (x1, y1), (x2, y2), (255, 255, 0), 2)

        dist = (h - y0 - maxi) * cfg.PIXEL_TO_CM_RATIO
        print(dist, (x1, y1), (x2, y2))
        return dist, (x1, y1), (x2, y2)
