"""Throwaway program to demonstrate color spaces and mapping 2D."""

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
        width = 810
        height = int(width / ratio)
    else:
        height = 810
        width = int(height * ratio)
    return image.resize((width, height))


def refactor_and_sort_data(color_data):
    """Covert RGB three-tuple and sort newly converted HLS data."""
    return sorted(color_data)


def main():
    """."""
    im = open_file_as_pil_image('test_imgs/leonardo_mona_lisa.jpg')

    width, height = im.size[0], im.size[1]

    if width > 1080 or height > 1080:
        im = resize_pil_image(im)

    rgb_data = im.getdata()
    sorted_hls_data = refactor_and_sort_data(rgb_data)

    sorted_im = create_empty_pil_image(im)
    sorted_im.putdata(sorted_hls_data)

    sorted_im.save('../wip/3Dsort/rgb_mona_lisa.png')


if __name__ == '__main__':
    main()
