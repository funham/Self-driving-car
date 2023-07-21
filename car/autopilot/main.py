import cv2
import cfg

from ticker import Ticker

from drivetrain.motor import Motor
from drivetrain.servo import Servo
from drivetrain.indication import Indication
from drivetrain.drivetrain import Drivetrain

from detection.detector import GlobalDetectionModel
from detection.detectors.road_detector import LaneLines
from detection.detectors.parking_detector import ParkingDetector

from autopilot import Autopilot
from frame import FrameMeta


if __name__ == '__main__':
    drivetrain = Drivetrain(power_pin=cfg.DRIVETRAIN_POWER_PIN,

                            motor=Motor(cfg.MOTOR_IN1_PIN,
                                        cfg.MOTOR_IN2_PIN,
                                        cfg.MOTOR_EN_PIN),

                            servo=Servo(cfg.SERVO_PIN),

                            indication=Indication(cfg.STOPLIGHT_PIN,
                                                  cfg.REVERSELIGHT_PIN,
                                                  cfg.L_BLINKER_PIN,
                                                  cfg.R_BLINKER_PIN)
                            )

    autopilot = Autopilot(drivetrain)
    detector = GlobalDetectionModel()
    cap = cv2.VideoCapture(0)

    detector.add_detector(LaneLines())
    detector.add_detector(ParkingDetector())

    try:
        while True:
            Ticker.update()

            ret, img = cap.read()
            detections_dict = detector.forward()

            frame = FrameMeta(img=img,
                              detections=detections_dict,
                              telemetry=drivetrain.telemetry_data)

            autopilot.feed(frame)
            drivetrain.update()

    finally:
        cap.release()
        print('goodbye')
