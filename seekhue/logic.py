from PIL import Image
from PIL import ImagePalette

def convert_image_to_PIL_Image_object(image):
    img = Image.open(image)
    return img
