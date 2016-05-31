"""Seekhue.py:."""

import colorsys

from PIL import Image


def open_file_as_pil_image(source_file):
    """Return a new Image object from source file."""
    return Image.open(source_file)


def create_empty_pil_image(pil_image):
    """Create an empty PIL Image."""
    return Image.new('RGB', (pil_image.size[0], pil_image.size[1]))


def resize_pil_image(image):
    """Resize PIL image object, fixing largest dimension to 1080px."""
    width, height = image.size[0], image.size[1]
    ratio = width / height
    if ratio >= 1:
        width, height = 1080, int(width / ratio)
    else:
        height, width = 1080, int(height * ratio)
    return image.resize((width, height))


def hls(x):
    """Transformation function.

    1. Refactors each Red Green and Blue value in our flattened list of pixel
    tuples to a number between 0 and 1.
    2. Uses the colorsys library to convert RGB values into Hue, Lightness,
    and Saturation.
    """
    to_float = lambda x: x / 255.0
    (r, g, b) = map(to_float, x)
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return h, l, s


def refactor_and_sort_data(color_data):
    """Covert RGB three-tuple and sort newly converted HLS data."""
    return sorted(color_data, key=hls)


def main():
    """Optional main for seekhue.py.

    1. Takes a jpg or png file as input and converts to PIL image.
    2. Checks image dimensions and sets largest dimension to 1080px.
    3. Returns RGB three-tuple of pixel color values.
    4. Sorts and converts RGB three-tuple into HSL three-tuple.
    5. Creates empty PIL image for sorted pixel data.
    6. Puts sorted pixel data into empty PIL image object.
    7. Saves Sorted image to disk.
    """
    im = open_file_as_pil_image('test_imgs/rothko_5.png')

    if im.size[0] > 1080 or im.size[1] > 1080:
        im = resize_pil_image(im)

    rgb_data = im.getdata()
    sorted_rgb_data = refactor_and_sort_data(rgb_data)

    sorted_im = create_empty_pil_image(im)
    sorted_im.putdata(sorted_rgb_data)

    sorted_im.save('test_imgs/hls_sort_rothko_5.png')


if __name__ == '__main__':
    main()
