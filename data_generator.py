import cv2
import numpy as np
import os

if __name__ == '__main__':


    blank = np.ones((200, 800, 3), dtype=np.uint8)
    blank *= 255
    result = blank.copy()

    text = '2019-05-27'

    '''
    FONT_HERSHEY_SIMPLEX = 0,
    FONT_HERSHEY_PLAIN = 1,
    FONT_HERSHEY_DUPLEX = 2,
    FONT_HERSHEY_COMPLEX = 3,
    FONT_HERSHEY_TRIPLEX = 4,
    FONT_HERSHEY_COMPLEX_SMALL = 5,
    FONT_HERSHEY_SCRIPT_SIMPLEX = 6,
    FONT_HERSHEY_SCRIPT_COMPLEX = 7,
    FONT_ITALIC = 16
    '''

    font = cv2.FONT_HERSHEY_SIMPLEX
    result = cv2.putText(img=result,
                         text=text,
                         org=(100, 100),
                         fontFace=16,
                         fontScale=3.2,
                         color=(0, 0, 0),
                         thickness=2,
                         lineType=cv2.LINE_AA)

    cv2.imshow('result', result)
    cv2.waitKey(0)
