import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ------------------------------------
#   Define display window configure
# ------------------------------------

row = 3
column = 3
gs = gridspec.GridSpec(3, 3)


def create_window(img, result, cdf_normalized, information):
    """ open window then separate image for comparison and add their label"""
    fig = plt.figure()
    fig.suptitle('Mammographic density measurement', fontsize=14, fontweight='bold')

    '''Show original image'''
    plt.subplot(gs[:, 0])
    plt.imshow(img)  # expects distorted color
    plt.title('Original')
    plt.xlabel('Input')

    '''Show result'''
    plt.subplot(gs[:, 1])
    plt.imshow(result)  # expect true color
    plt.title('Threshold')
    plt.xlabel('Output')

    '''Display calculation part'''
    ax = fig.add_subplot(gs[0, 2])
    ax.set_title('Calculation')

    breast = 'Breast area = ' + str(information[0][1])
    tissue = 'Tissue area = ' + str(information[1][1])
    density = "%10.3f" % information[2][1]
    density += " %"

    ax.text(0.05, 0.8, breast, fontsize=9)
    ax.text(0.05, 0.6, tissue, fontsize=9)
    ax.text(0.05, 0.4, 'Density =' + density, fontsize=9)
    plt.xticks([])
    plt.yticks([])
    # plt.axis('off') # Remove frame

    '''Show histogram'''
    plt.subplot(gs[1:, 2]).plot(cdf_normalized, color='b')
    plt.hist(img.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.ylim([-50, 20000])
    plt.legend(('cdf', 'histogram'), loc='upper right')

    '''Maximize window'''
    mng = plt.get_current_fig_manager()
    # mng.full_screen_toggle() # Full-screen
    mng.window.state('zoomed')

    plt.show()
