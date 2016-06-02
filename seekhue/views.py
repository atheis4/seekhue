"""Seek Hue: views.py."""

from django.http import HttpResponse
from django.shortcuts import render

from . import logic


def render_painting(request, painting_id):
    """."""
    painting = logic.return_painting_by_id(painting_id)
    template_args = {
        'painting': painting,
    }
    return render(request, 'seekhue/painting.html', template_args)


def render_index(request):
    """Render index with previously transformed images in django template."""
    painting_list = logic.return_paintings_from_db()

    template_args = {
        'painting_list': painting_list,
    }
    return render(request, 'seekhue/index.html', template_args)


def render_form(request):
    """Docstring."""
    return render(request, 'seekhue/form.html', {})


def render_ack(request):
    """."""
    artist = request.POST['artist']
    title = request.POST['title']
    data = request.POST['data']
    img_file = request.FILES['image-source']

    pil_image = logic.create_and_resize_pil_image(img_file)
    sorted_pil_image = logic.create_sorted_pil_image(pil_image)

    original_django_file = logic.create_django_file(pil_image)
    sorted_django_file = logic.create_django_file(sorted_pil_image)

    django_file_tuple = logic.name_django_file_objects(
        title,
        original_django_file,
        sorted_django_file
    )

    painting = logic.create_painting_model(
        django_file_tuple,
        artist,
        title,
        data,
    )
    template_args = {
        'painting': painting,
    }
    return render(request, 'seekhue/ack.html', template_args)


def render_about(request):
    """."""
    return render(request, 'seekhue/about.html', {})
