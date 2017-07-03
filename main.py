import cv2
import windowmanager as window
import breast_segmentation as bs

# ------------------------------------
#   Mammographic density measurement
# ------------------------------------

information = []

'''Open image'''
img_name = raw_input("Please select image -> ")
# origin_img = 'image/MLO_test.bmp'
origin_img = 'image/' + img_name

'''Threshold & Contour'''
img = cv2.imread(origin_img)
img2, breast_area = bs.breast_display(img)
t = bs.otsu_threshold_value(img2)  # Find threshold value from Otsu's method
# t = input("Threshold value -> ")   # Specify threshold value
img3, tissue_area = bs.glandular_tissue_display(img2, t)

density = (tissue_area / breast_area) * 100
information.append(("Breast area", breast_area))
information.append(("Glandular tissue area", tissue_area))
information.append(("Density", density))
information.append(("Threshold value", t))

print "Threshold value= ", t
print "Breast area = ", breast_area
print "Glandular tissue area = ", tissue_area
print "Density = %10.3f" % density, " %"

'''normalized image to create histogram'''
cdf_normalized = bs.image_histogram(img)

window.create_window(img2, img3, cdf_normalized, information)
