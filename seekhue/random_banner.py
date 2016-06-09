"""Produce a randomly generated banner for SeekHue website."""

import colorsys
import random

from PIL import Image


def create_pil_image():
    """."""
    width, height = 32, 4
    dimensions = width, height
    return Image.new('RGB', (dimensions))


def generate_random_pixels():
    """."""
    pixel_data = []

    for i in range(4):
        for pixel in range(32):
            x = random.randint(0, 255)
            y = random.randint(0, 255)
            z = random.randint(0, 255)
            rgb = (x, y, z)
            pixel_data.append(rgb)

    return pixel_data


def hls(x):
    """."""
    to_float = lambda x: x / 255
    (r, g, b) = map(to_float, x)
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    h = h if 0 < h else 1
    return h, l, s


def convert_and_sort_pixel_data(pixel_data):
    """."""
    return sorted(pixel_data, key=hls, reverse=True)


def resize_pil_image(pil_image):
    """."""
    width, height = 1440, 180
    dimensions = width, height
    return pil_image.resize(dimensions)


def main():
    """."""
    background_image = create_pil_image()
    pixel_data = generate_random_pixels()
    sorted_pixels = convert_and_sort_pixel_data(pixel_data)

    background_image.putdata(sorted_pixels)
    background_image = resize_pil_image(background_image)

    return background_image


if __name__ == '__main__':
    main()
