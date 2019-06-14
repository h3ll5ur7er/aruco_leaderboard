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

    def __call__(self, stream):
        stream.seek(0)
        file_bytes = np.asarray(bytearray(stream.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        corners, ids, rejectedImgPoints = ar.detectMarkers(img, self.dictionary)
        markers = []
        
        if ids is not None:
            c = corners[0][0]
            
            left = c[1] - c[0]
            down = c[3] - c[0]

            mat = np.array([[left, down]])
            inv_mat = inv(mat)

        ids = ids if ids is not None else []
        positions = []
        for idx, _id in enumerate(ids):
            markers.append(Marker(_id[0], corners[idx][0], inv_mat))
            positions.append(markers[-1].position)
        min_x = 1000000000
        max_x = -1000000000
        min_y = 1000000000
        max_y = -1000000000
        for pos in positions:
            y, x = pos[0]
            min_x = min([min_x, x])
            max_x = max([max_x, x])
            min_y = min([min_y, y])
            max_y = max([max_y, y])
        pivot_x = (max_x + min_x)/2
        pivot_y = (max_y + min_y)/2
        ordered_marker_ids = [None,]*len(markers)
        for m in markers:
            y, x = m.position[0]
            # print("m:", m.value)
            # h_pos = None
            # v_pos = None
            if y<pivot_y:
                # h_pos = "left"
                
                if x<pivot_x:
                    # v_pos = "upper"
                    ordered_marker_ids[0] = m.value
                else:
                    # v_pos = "lower"
                    ordered_marker_ids[3] = m.value
            else:
                # h_pos = "right"
                
                if x<pivot_x:
                    # v_pos = "upper"
                    ordered_marker_ids[1] = m.value
                else:
                    # v_pos = "lower"
                    ordered_marker_ids[2] = m.value
        return ordered_marker_ids
