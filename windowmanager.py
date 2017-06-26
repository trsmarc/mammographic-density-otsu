import matplotlib.pyplot as plt

# ------------------------------------
#   Define display window configure
# ------------------------------------

row = 1
column = 3


def create_window(img, result, cdf_normalized):
    """ open window then separate image for comparison and add their label"""

    plt.subplot(row, column, 1)
    plt.imshow(img)  # expects distorted color
    plt.title('Original')
    plt.xlabel('Input')

    plt.subplot(row, column, 2)
    plt.imshow(result)  # expect true color
    plt.title('Threshold')
    plt.xlabel('Output')

    # show image histogram
    # plt.subplot(row, column, 3)
    # plt.hist(img.ravel(), 256, [0, 256])

    # ----------------------
    # Show histogram
    # ----------------------
    plt.subplot(row, column, 3).plot(cdf_normalized, color='b')
    plt.hist(img.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.ylim([-50, 20000])
    plt.legend(('cdf', 'histogram'), loc='upper right')

    plt.show()
