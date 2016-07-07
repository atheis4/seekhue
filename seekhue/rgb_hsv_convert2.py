"""."""
from PIL import Image

class Image(object):
    """docstring for Image"""
    def __init__(self, artist, title, pixel_list):
        self.artist = artist
        self.title = title
        self.pixels = pixel_list


class Pixel(object):
    """."""
    def __init__(self, hue, sat, val):
        self.hue = hue
        self.sat = sat
        self.val = val

    def __str__(self):
        return 'Pixel(hue: {}, saturation: {}, value: {})'.format(
            self.hue, self.sat, self.val
        )


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
    source = 'munch_1.jpg'
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
    # print(list(color_data_rgb))

    color_data_hsv = [rgb_to_hsv(r, g, b) for (r, g, b) in color_data_rgb]
    # print(list(color_data_hsv))

# dict = {h : {s, v: tuple}}

    hue_to_count = {}
    hue_list = []
    hue_set = ()
    for h, s, v in color_data_hsv:
        if h not in hue_to_count:
            hue_to_count[h] = {}
        if s not in hue_to_count[h]:
            hue_to_count[h][s] = {}
        if v not in hue_to_count[h][s]:
            hue_to_count[h][s][v] = 1
        hue_to_count[h][s][v] += 1

    print(hue_to_count.items())
    print('-----')
    print(hue_to_count.keys())
    print('-----')
    print(len(hue_to_count.keys()))
    print(len(hue_to_count))
    print(width * height)

    # print(hue_to_count)
    # print(len(hue_to_count))


if __name__ == '__main__':
    main()
