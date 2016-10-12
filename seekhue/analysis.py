"""."""

from PIL import Image


class Pixel(object):
    """."""

    def __init__(self, hsv, rgb):
        """Pixel initialization.

        hsv: list of pixel values, tuple of hue, saturation, and value
        rgb: list of pixel values, tuple of red, blue, green values
        """
        self.hsv = hsv
        self.rgb = rgb

    def __repr__(self):
        """."""
        return 'Pixel(hsv: {}, rgb: {})'.format(
            self.hsv, self.rgb
        )

    def __eq__(self, other):
        """."""
        return(
            self.hsv == other.hsv and
            self.rgb == other.rbg
        )


def open_pil_image(source):
    """."""
    return Image.open(source)


def rgb_to_hsv(r, g, b):
    """Convert rgb tuple into hsv tuple.

    input:
    r, g, b:    int
        tuple of values between 0-255

    output:
    h, s, v:    float
        tuple of values between 0-1

    To convert RGB color space into HSV color space:

    R' = R / 255.0
    G' = G / 255.0
    B' = B / 255.0
    Cmax = max(R', G', B')
    Cmin = min(R', G', B')
    Difference = Cmax - Cmin
    """
    # Divide each value by 255 to refactor it as a new float between 0 and 1
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    # Identify maximum r, g, b value
    max_val = max(r, g, b)
    # Identify minimum r, g, b value
    min_val = min(r, g, b)
    # Identify the difference between the maximum and minimum r, g, b values
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


def rgb_to_hls(r, g, b):
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

    l = (max_val + min_val) / 2

    if max_val == 0:
        s = 0
    else:
        s = difference / (1 - abs((2 * l) - 1))

    return h, l, s


def main():
    """."""
    source = 'test_imgs/van_gogh_starry_night.jpg'
    pil_im = open_pil_image(source)
    width, height = pil_im.size[0], pil_im.size[1]
    ratio = width / height

    if ratio > 1:
        width = 270
        height = int(width / ratio)
    else:
        height = 270
        width = int(height * ratio)

    pil_im = pil_im.resize((width, height))

    color_data_rgb = pil_im.getdata()

    color_data_hsv = [rgb_to_hsv(r, g, b) for (r, g, b) in color_data_rgb]

# Zero Division Error
    # color_data_hls = [rgb_to_hls(r, g, b) for (r, g, b) in color_data_rgb]

    color_rgb_float = [(r / 255.0, g / 255.0, b / 255.0) for (r, g, b) in color_data_rgb]

    # classes

    equal = 0


if __name__ == '__main__':
    main()
