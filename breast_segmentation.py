import cv2
import numpy as np


# ------------------------------------
#   Breast Region Segmentation
# ------------------------------------


def breast_display(img):
    """ Respresent breast part """

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hist = get_histogram_max_value(img)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return thresh


def get_histogram_max_value(img):
    hist, bins = np.histogram(img.flatten(), 256, [0, 255])
    return hist


def image_histogram(img):
    hist = get_histogram_max_value(img)
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()
    return cdf_normalized
