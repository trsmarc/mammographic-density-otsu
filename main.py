import cv2
import windowmanager as window
import breast_segmentation as bs

img = cv2.imread('image/MLO_test.bmp')
img2 = bs.breast_display(img)

window.create_window(img, img2)
