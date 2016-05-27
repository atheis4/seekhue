"""Seekhue.py:."""

import colorsys

from PIL import Image


def open_file_as_pil_image(source_file):
    """Return a new Image object from source file."""
    return Image.open(source_file)


def create_empty_pil_image(pil_image):
    """Create an empty PIL Image.

    Returns an empty PIL image with the same dimensions as the first PIL Image.
    """
    return Image.new('RGB', (pil_image.size[0], pil_image.size[1]))


def resize_pil_image(image):
    """Resize PIL image object, fixing largest dimension to 1080px."""
    width = image.size[0]
    height = image.size[1]
    ratio = width / height
    if ratio >= 1:
        width = 1080
        height = int(width / ratio)
    else:
        height = 1080
        width = int(height * ratio)
    return image.resize((width, height))


def get_data_from_pil_image(pil_image):
    """Return a flattened, three-tuple of RGB values between 0 and 255."""
    return pil_image.getdata()


def hls(x):
    """."""
    to_float = lambda x: x / 255.0
    (r, g, b) = map(to_float, x)
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    h = h if h > 0 else 1
    return h, l, s


def refactor_and_sort_data(color_data):
    """Input: a flattened list of an RGB three-tuple."""
    return sorted(color_data, key=hls)


def main():
    """Fill Docstring."""
    im = open_file_as_pil_image('test_imgs/008.010.6.1_206.png')

    if im.size[0] > 1080 or im.size[1] > 1080:
        im = resize_pil_image(im)

    rgb_data = get_data_from_pil_image(im)
    sorted_rgb_data = refactor_and_sort_data(rgb_data)

    sorted_im = create_empty_pil_image(im)
    sorted_im.putdata(sorted_rgb_data)

    sorted_im.save('test_imgs/hls_sort_008.010.6.1_206.png')


if __name__ == '__main__':
    main()
