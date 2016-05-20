from PIL import Image
from PIL import ImagePalette

im = Image.open('../codeguild/frontend/img/008.102.1.2_2768.png')
im2 = Image.open('../codeguild/frontend/img/008.102.1.2_2768.png').convert('P')

print(im.format, im.size, im.mode)

print(im2.format, im2.size, im2.mode)

print(sorted(im2.getpalette()))


px = im.load()

im.show()
