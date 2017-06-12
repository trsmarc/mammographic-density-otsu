import matplotlib.pyplot as plt

# ------------------------------------
#   Define display window configure
# ------------------------------------

row = 1
column = 2


def create_window(img, result):
    """ open window then separate image for comparison and add their label"""


    plt.subplot(row, column, 1)
    plt.imshow(img)  # expects distorted color
    plt.title('Original')
    plt.xlabel('Input')

    plt.subplot(row, column, 2)
    plt.imshow(result)  # expect true color
    plt.title('Segmented')
    plt.xlabel('Output')

    plt.show()
