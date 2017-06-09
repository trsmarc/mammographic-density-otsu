import cv2
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------
#   Define display window configure
# ------------------------------------

row = 1
column = 2
img = cv2.imread('image/MLO_test.bmp')

img2 = img  # do something with img2

kernel = np.ones((5,5),np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

plt.subplot(row, column, 1)
plt.imshow(img)  # expects distorted color
plt.title('Original')
plt.xlabel('Input')

plt.subplot(row, column, 2)
plt.imshow(closing)  # expect true color
plt.title('Segmented')
plt.xlabel('Output')

plt.show()
