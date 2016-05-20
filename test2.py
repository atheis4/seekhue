from PIL import Image
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

img = Image.open('austrian_flag_test.png')
arr = np.array(img)
print(arr)

img2 = Image.fromarray(arr)

arr2 = np.sort(arr)
print()
print(arr2)

img3 = Image.fromarray(arr2)

plt.imshow(img)

print(len(arr))
ratio_x_to_y = img.size[0]/img.size[1]
print(arr[533:534])
