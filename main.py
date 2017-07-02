import cv2
import windowmanager as window
import breast_segmentation as bs

# ------------------------------------
#   Mammographic density measurement
# ------------------------------------

information = []

'''Open image'''
# origin_img = 'image/MLO_test.bmp'
origin_img = 'image/02.png'

'''Threshold & Contour'''
img = cv2.imread(origin_img)
img2, breast_area = bs.breast_display(img)
img3, tissue_area = bs.glandular_tissue_display(img2)

density = (tissue_area / breast_area) * 100
information.append(("Breast area", breast_area))
information.append(("Glandular tissue area", tissue_area))
information.append(("Density", density))
print "Breast area = ", breast_area
print "Glandular tissue area = ", tissue_area
print "Density = %10.3f" % density, " %"

'''normalized image to create histogram'''
cdf_normalized = bs.image_histogram(img2)

window.create_window(img2, img3, cdf_normalized, information)
