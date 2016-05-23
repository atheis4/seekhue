import random
from PIL import Image

colors_length = 1000
colors = []
for i in range(1, colors_length):
    colors.append(
        [
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        ]
    )

colors.sort()
