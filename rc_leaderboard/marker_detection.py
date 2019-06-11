import numpy as np
import cv2
import cv2.aruco as ar
from .framework import Singleton
class MarkerDetector(metaclass=Singleton):
    def __init__(self, marker_dict:int=3):
        """
        type: one ofthe following
            DICT_4X4_100 = 1
            DICT_4X4_1000 = 3
            DICT_4X4_250 = 2
            DICT_4X4_50 = 0
            DICT_5X5_100 = 5
            DICT_5X5_1000 = 7
            DICT_5X5_250 = 6
            DICT_5X5_50 = 4
            DICT_6X6_100 = 9
            DICT_6X6_1000 = 11
            DICT_6X6_250 = 10
            DICT_6X6_50 = 8
            DICT_7X7_100 = 13
            DICT_7X7_1000 = 15
            DICT_7X7_250 = 14
            DICT_7X7_50 = 12
            DICT_ARUCO_ORIGINAL = 16
        """
        self.dictionary = ar.getPredefinedDictionary(marker_dict)

    def __call__(self, stream):
        print(type(stream))
        print(stream)
        stream.seek(0)
        file_bytes = np.asarray(bytearray(stream.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        corners, ids, rejectedImgPoints = ar.detectMarkers(img, self.dictionary)
        return ids
