"""Logic.py."""

import io

from django.core.files import File

from . import models
from . import seekhue


def create_painting_model_from_file(img_file, sorted_img_file):
    """Docstring for f(x)."""
    new_painting = models.Painting(
        source=img_file,
    )
    new_painting.seekhue_sort.save('somename', sorted_img_file)
    new_painting.save()


def return_paintings_from_db():
    """Docstring for f(x)."""
    return models.Painting.objects.all()


def return_painting_by_id(id):
    """."""
    return models.Painting.objects.get(id=id)


def return_sorted_jpg_object(img_file):
    """."""
    im = seekhue.open_file_as_pil_image(img_file)

    if im.size[0] > 1080 or im.size[1] > 1080:
        im = seekhue.resize_pil_image(im)

    rgb_data = seekhue.get_data_from_pil_image(im)
    sorted_rgb_data = seekhue.refactor_and_sort_data(rgb_data)

    sorted_im = seekhue.create_empty_pil_image(im)
    sorted_im.putdata(sorted_rgb_data)

    temporary_jpg_file = File(io.BytesIO())
    sorted_im.save(temporary_jpg_file, format='jpeg')
    return temporary_jpg_file
