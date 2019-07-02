import cv2
import numpy as np
from .framework import Singleton

class Camera(metaclass=Singleton):
    def __init__(self):
        self._cap = cv2.VideoCapture(0)
    def grab(self):
        success, frame = self._cap.read()
        return frame if success else None

    def save(self, path):
        frame = self.grab()
        if frame is not None:
            cv2.imwrite(path, frame)
