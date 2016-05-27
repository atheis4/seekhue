"""Rearranger.py Docstring."""

from PIL import Image


def open_image(source):
    """Fill Docstring."""
    return Image.open(source)


def resize_img(image):
    """Fill Docstring."""
    ratio = image.size[0] / image.size[1]
    width = 1080
    height = int(width / ratio)
    return image.resize((width, height))


def get_data_from_im(image):
    """Fill Docstring."""
    return image.getdata()


def create_new_img_for_sort(image):
    """Fill Docstring."""
    return Image.new('RGB', (image.size[0], image.size[1]))


def sort_rgb_to_grb(image):
    """Fill Docstring."""
    reverse_data = []

    for r, g, b in image.getdata():
        reverse_data.append((b, r, g))

    return reverse_data


def main():
    """."""
    im = open_image('test_imgs/ernst_1.jpg')

    if im.size[0] > 1080:
        im = resize_img(im)

    reverse_data = sort_rgb_to_grb(im)

    new_im = create_new_img_for_sort(im)
    new_im.putdata(reverse_data)

    new_im.show()
    new_im.save('test_imgs/BRG_ernst_1.jpg')


if __name__ == '__main__':
    main()
