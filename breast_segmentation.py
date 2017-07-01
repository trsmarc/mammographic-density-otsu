import cv2
import numpy as np


# ------------------------------------
#   Breast Region Segmentation
# ------------------------------------


def breast_display(img):
    """ Respresent breast part """
    # hist = get_histogram_max_value(img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)

    # contour breast part
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    contour_area_list = [len(contours)]
    count = 0
    for i in contours:
        area = cv2.contourArea(i)
        contour_area_list.append(area)
        print "contour index ", count, " area = ", area
        count += 1

    max_area_index = contour_area_list.index(max(contour_area_list)) - 1
    print max(contour_area_list)
    print max_area_index
    cv2.drawContours(img, contours, max_area_index, (255, 0, 0), 3)

    return im2


def get_histogram_max_value(img):
    hist, bins = np.histogram(img.flatten(), 256, [0, 255])
    return hist


def image_histogram(img):
    hist = get_histogram_max_value(img)
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()
    return cdf_normalized
