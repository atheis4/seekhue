"""Seek Hue: views.py."""

from django.http import HttpResponse
from django.shortcuts import render

from . import logic


def my_image(request):
    """Test to send an HTTP Response object with an image."""
    image_data = open('test_imgs/cezanne_1.jpg', 'rb')
    return HttpResponse(image_data, content_type='image/jpg')


def render_index(request):
    """Render index with previously transformed images in django template."""
    image_list = logic.return_paintings_from_db()

    template_args = {
        'image_list': image_list,
    }

    return render(request, 'seekhue/index.html', template_args)


def render_form(request):
    """Docstring."""
    return render(request, 'seekhue/form.html', {})


def render_ack(request):
    """."""
    img_file = request.FILES['image-source']

    pil_image = logic.create_and_resize_pil_image(img_file)
    sorted_pil_image = logic.create_sorted_pil_image(pil_image)

    original_django_file = logic.create_django_file(pil_image)
    sorted_django_file = logic.create_django_file(sorted_pil_image)

    django_file_tuple = logic.name_django_file_objects(
        img_file,
        original_django_file,
        sorted_django_file
    )
    logic.create_painting_model(django_file_tuple)

    return render(request, 'seekhue/ack.html', {})
