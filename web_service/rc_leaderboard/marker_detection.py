import numpy as np
from numpy.linalg import inv
import cv2
import cv2.aruco as ar
from pprint import pprint
from .framework import Singleton

class Marker:
    def __init__(self, value, corners, transform=np.eye(2)):
        self.value = value
        self.corners = corners
        self.position = self.corners[0].dot(transform)
    def __str__(self):
        return "Marker(value={}, position={})".format(self.value, self.position)
    def __repr__(self):
        return str(self)


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
        
    def normalize_markers(self, ids, corners):
        markers = []
        
        if ids is not None:
            c = corners[0][0]
            
            left = c[1] - c[0]
            down = c[3] - c[0]

            mat = np.array([[left, down]])
            transform = inv(mat)

        ids = ids if ids is not None else []
        
        for idx, _id in enumerate(ids):
            markers.append(Marker(_id[0], corners[idx][0], transform))
        return markers

    def order_markers(self, markers):
        min_x = 1000000000
        max_x = -1000000000
        min_y = 1000000000
        max_y = -1000000000
        for pos in map(lambda m: m.position, markers):
            y, x = pos[0]
            min_x = min([min_x, x])
            max_x = max([max_x, x])
            min_y = min([min_y, y])
            max_y = max([max_y, y])
        pivot_x = (max_x + min_x)/2
        pivot_y = (max_y + min_y)/2
        ordered_markers = [None,]*len(markers)
        for m in markers:
            y, x = m.position[0]
            # print("m:", m.value)
            # h_pos = None
            # v_pos = None
            if y<pivot_y:
                # h_pos = "left"
                
                if x<pivot_x:
                    # v_pos = "upper"
                    ordered_markers[0] = m
                else:
                    # v_pos = "lower"
                    ordered_markers[3] = m
            else:
                # h_pos = "right"
                
                if x<pivot_x:
                    # v_pos = "upper"
                    ordered_markers[1] = m
                else:
                    # v_pos = "lower"
                    ordered_markers[2] = m
        return order_markers

    def image_from_stream(self, stream):
        stream.seek(0)
        file_bytes = np.asarray(bytearray(stream.read()), dtype=np.uint8)
        return cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    def detect_ordered_markers(self, img):
        corners, ids, rejectedImgPoints = ar.detectMarkers(img, self.dictionary)
        markers = self.normalize_markers(ids, corners)
        ordered_markers = self.order_markers(markers)
        return order_markers

    def __call__(self, stream):
        img = self.image_from_stream(stream)
        ordered_markers = self.detect_ordered_markers(img)
        ordered_marker_ids = list(map(lambda m:m.value, order_markers))
        return ordered_marker_ids
