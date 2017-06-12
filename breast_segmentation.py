import cv2
import numpy as np

# ------------------------------------
#   Breast Region Segmentation
# ------------------------------------


def breast_display(img):
    """ Respresent breast part """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    kernel = np.ones((3, 3), np.uint8)
    result = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
    return result
