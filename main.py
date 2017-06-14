import cv2
import windowmanager as window
import breast_segmentation as bs

origin_img = 'image/MLO_test.bmp'

img = cv2.imread(origin_img)
img2 = bs.breast_display(img)

window.create_window(img, img2)
