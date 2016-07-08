from pil import Image

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
        width = 1080
        height = int(width / ratio)
    else:
        height = 1080
        width = int(height * ratio)
    return image.resize((width, height))

def color_swap(color_data):
    """."""
    
