
from .framework import Singleton
import cv2

class MarkerRegistry(metaclass=Singleton):
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
    def __init__(self, **marker_settings):
        self._marker_settings = marker_settings
        self._next_marker_id = 0
        
        if "type" not in self._marker_settings:
            self._marker_settings["type"] = 3
        
        self._marker_dictionary = cv2.aruco.getPredefinedDictionary(self._marker_settings["type"])

    def get_marker_for(self, id:int, size_in_pixels:int=256, format:str=".png"):
        img = self._marker_dictionary.drawMarker(id, size_in_pixels)
        rv, buff = cv2.imencode(format, img)
        if rv:
            return bytes(buff)
        else:
            return None

    def invalidate_marker(self, id):
        self._next_marker_id = id + 1

    def get_next_marker(self, invalidate:bool=True):
        marker = None
        while marker is None and self._next_marker_id<1000:
            marker = self.get_marker_for(self._next_marker_id)
        self.invalidate_marker(self._next_marker_id)
        return marker
