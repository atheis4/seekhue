"""Seek Hue: views.py."""

from django.http import HttpResponse
from django.shortcuts import render

from . import logic


def my_image(request):
    """Test to send an HTTP Response object with an image."""
    image_data = open('test_imgs/cezanne_1.jpg', 'rb')
    return HttpResponse(image_data, content_type='image/jpg')


def render_index(request):
    """Docstring."""
    image_list = logic.return_paintings_from_db()

    template_args = {
        'image_list': image_list,
    }

    return render(request, 'seekhue/index.html', template_args)


def render_form(request):
    """Docstring."""
    return render(request, 'seekhue/form.html', {})


def render_ack(request):
    """Docstring."""
    img_file = request.FILES['image-source']
    sorted_jpg_file = logic.return_sorted_jpg_object(img_file)

    logic.create_painting_model_from_file(img_file, sorted_jpg_file)

    return render(request, 'seekhue/ack.html', {})
