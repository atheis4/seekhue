from PIL import Image, ImageDraw
import colorsys

def make_rainbow_rgb(colors, width, height):
    '''colors is an array of RGB tuples, with values bewteen 0 and 255'''
    img = Image.new('RGBA', (width, height))
    canvas = ImageDraw.Draw(img)

    def hsl(x):
        to_float = lambda x: x / 255.0
        (r, g, b) = map(to_float, x)
        h, s, l = colorsys.rgb_to_hsv(r, g, b)
        h = h if 0 < h else 1
        return h, s, l

    rainbow = sorted(colors, key=hsl)

    dx = width / float(len(colors))
    x = 0
    y = height / 2.0
    for rgb in rainbow:
        canvas.line((x, y, x + dx, y), width=height, fill=rgb)
        x += dx

    img.show()
