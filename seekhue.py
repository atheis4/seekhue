from PIL import Image
import colorsys

def open_image(source):
    return Image.open(source)

def resize_image(image):
    ratio = image.size[0] / image.size[1]
    width = 1080
    height = int(width / ratio)
    return image.resize((width, height))

def get_color_data_from_image(image):
    return image.getdata()

def hsv(x):
    to_float = lambda x: x / 255.0
    (r, g, b) = map(to_float, x)
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    h = h if 0 < h else 1
    return h, s, v

def hls(x):
    to_float = lambda x: x / 255.0
    (r, g, b) = map(to_float, x)
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    h = h if 0 < h else 1
    return h, l, s


def main():
    im = open_image('test_imgs/van_gogh_starry_night.jpg')

    if im.size[0] > 1080:
        im = resize_image(im)

    data = get_color_data_from_image(im)

    rainbow = sorted(data, key=hsv)

    new_image = Image.new('RGB', (im.size[0], im.size[1]))
    new_image.putdata(rainbow)

    new_image.show()



if __name__=="__main__":
    main()
