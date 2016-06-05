"""Logic.py."""

import io

from django.core.files import File

from . import models
from . import seekhue


def create_and_resize_pil_image(img_file):
    """Open image file as PIL Image and resize if necessary."""
    pil_image = seekhue.open_file_as_pil_image(img_file)

    if pil_image.size[0] > 1080 or pil_image.size[1] > 1080:
        pil_image = seekhue.resize_pil_image(pil_image)

    return pil_image


def create_sorted_pil_image(pil_image):
    """Extract, sort, and place refactored pixel data into new PIL object.

    Takes a PIL Image as input to extract pixel data from and use as
    template for empty PIL Image oject.
    """
    pixel_data = pil_image.getdata()
    sorted_pixel_data = seekhue.refactor_and_sort_data(pixel_data)

    sorted_pil_image = seekhue.create_empty_pil_image(pil_image)
    sorted_pil_image.putdata(sorted_pixel_data)
    return sorted_pil_image


def create_django_file(pil_img):
    """Create a django compatable file object of a pil image."""
    django_file = File(io.BytesIO())
    pil_img.save(django_file, format='jpeg')

    return django_file


def name_django_file_objects(title, original_file_obj, sorted_file_obj):
    """Set name property for django file obejcts."""
    file_name = title

    original_file_obj.name = file_name
    sorted_file_obj.name = 'sorted_' + file_name

    return (original_file_obj, sorted_file_obj)


def create_painting_model(file_obj_tuple, artist, title, data):
    """Take a tuple of django compatible files and create painting model."""
    original_file, sorted_file = file_obj_tuple[0], file_obj_tuple[1]
    new_painting = models.Painting(
        source=original_file,
        seekhue_sort=sorted_file,
        artist=artist,
        title=title,
        data=data,
    )
    new_painting.save()
    return new_painting


def return_paintings_from_db():
    """."""
    return models.Painting.objects.all().order_by('-timestamp')[:9]


def return_painting_by_id(painting_id):
    """."""
    # print(painting_id)
    return models.Painting.objects.get(id=painting_id)
