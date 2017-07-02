import cv2
import windowmanager as window
import breast_segmentation as bs

# ------------------------------------
#   Mammographic density measurement
# ------------------------------------

'''Open image'''
origin_img = 'image/MLO_test.bmp'
# origin_img = 'image/05.png'

'''Threshold & Contour'''
img = cv2.imread(origin_img)
img2 = bs.breast_display(img)
img3 = bs.glandular_tissue_display(img2)

'''normalized image to create histogram'''
cdf_normalized = bs.image_histogram(img2)

window.create_window(img2, img3, cdf_normalized)
