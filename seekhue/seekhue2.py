"""Seekhue.py:."""

from __future__ import division

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


def refactor_color_data(color_data):
    """Take a list of RGB tuples and divide each value by 255."""
    refactored_data = [(r / 255.0, g / 255.0, b / 255.0) for (r, g, b) in color_data]
    return refactored_data


def convert_refactored_rgb_data_to_hls(refactored_data):
    """Convert refactored RGB tuples into HLS tuples."""
    # hls_data = [colorsys.rgb_to_hls(r, g, b) for (r, g, b) in refactored_data]

    hls_data = []

    for (r, g, b) in refactored_data:
        h, l, s = colorsys.rgb_to_hls(r, g, b)
        hls_data.append((h, l, s))

    return hls_data


def multiply_hls_by_255(hls_data):
    """Multiply each HLS value by 255 to un-refactor after conversion."""
    un_factored_hls = [(int(h * 255), int(l * 255), int(s * 255)) for (h, l, s) in hls_data]
    return un_factored_hls


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
    im = open_file_as_pil_image('test_imgs/munch_1.jpg')

    width, height = im.size[0], im.size[1]

    if width > 1080 or height > 1080:
        im = resize_pil_image(im)

    rgb_data = im.getdata()

    new_color_data = refactor_color_data(rgb_data)
    hls_color_data = convert_refactored_rgb_data_to_hls(new_color_data)

    sorted_hls_data = sorted(hls_color_data)

    sorted_hls_data = multiply_hls_by_255(sorted_hls_data)

    print('original pixel data form: ' + str(rgb_data[0]))
    print('sorted, hls data form: ' + str(sorted_hls_data[0]))

    sorted_im = create_empty_pil_image(im)
    sorted_im.putdata(sorted_hls_data)

    sorted_im.show()

    # sorted_im.save('test_imgs/hls_sort_munch_1.png')


if __name__ == '__main__':
    main()
