from PIL import Image
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

img = Image.open('austrian_flag_test.png')
arr = np.array(img)
# print(arr)

img2 = Image.fromarray(arr)

arr2 = np.sort(arr)
print()
# print(arr2)

img3 = Image.fromarray(arr2)

plt.imshow(img)

print(len(arr))
ratio_x_to_y = img.size[0]/img.size[1]
# print(img.mode)
# print(arr[0])
# print(arr[0][0])

raw_pixels = [[90, 108, 6], [104, 25, 120], [255, 0, 0], [0, 255, 0]]

data = list(sorted(img.getdata()))
print(img.size)

new_img = Image.new('RGB', (1600, 1067))

new_img.putdata(data)

new_img.show()
