"""."""
from PIL import Image


def open_pil_image(source):
    """."""
    return Image.open(source)

def rgb_to_hsv(r, g, b):
    """."""
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    max_val = max(r, g, b)
    min_val = min(r, g, b)
    difference = max_val - min_val

    if max_val == min_val:
        h = 0
    elif max_val == r:
        h = (60 * ((g - b) / difference) + 360) % 360
    elif max_val == g:
        h = (60 * ((b - r) / difference) + 120) % 360
    elif max_val == b:
        h = (60 * ((r - g) / difference) + 240) % 360
    if max_val == 0:
        s = 0
    else:
        s = difference / max_val

    v = max_val
    return h, s, v


def main():
    """."""
    source = '../test_imgs/munch_1.jpg'
    pil_im = open_pil_image(source)
    pil_im.show()

    color_data_rgb = pil_im.getdata()
    # print(list(color_data_rgb))

    color_data_hsv = [rgb_to_hsv(r, g, b) for (r, g, b) in color_data_rgb]
    # print(list(color_data_hsv))

if __name__ == '__main__':
    main()
