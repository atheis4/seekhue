"""Analysis module for SeekHue Color Quantizer."""

import colorsys

import seekhue

from PIL import Image

source = '../test_imgs/van_gogh_starry_night.jpg'

sorted_im = seekhue.main(source)

sorted_im.show()
