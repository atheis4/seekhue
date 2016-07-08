"""Seek Hue: views.py."""

from django.http import HttpResponse
from django.shortcuts import render

from . import logic


def render_painting(request, painting_id):
    """Render an individual painting by model id."""
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


def render_ack(request):
    """Process form submission.

    Take in form field arguments.
    Create original pil image from image source.
    Create sorted pil image from original pil image.
    Convert original and sorted pil images into Django compatable files.
    Create a tuple of Django file objects and name them.
    Input data into Painting model and save the instance of the model.
    """
    artist = request.POST['artist']
    title = request.POST['title']
    year = request.POST['year']
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
        year,
        data,
    )
    template_args = {
        'painting': painting,
    }
    return render(request, 'seekhue/ack.html', template_args)


def render_about(request):
    """Render about page."""
    return render(request, 'seekhue/about.html', {})


def render_search(request):
    """Take search term and query database, returning hits."""
    search_term = request.GET['search']

    painting_list = logic.return_painting_by_search(search_term)

    template_args = {
        'painting_list': painting_list,
    }
    return render(request, 'seekhue/search.html', template_args)


def render_random_img(request):
    """Return random header/footer banner as HTTP object."""
    response = HttpResponse(content_type='image/jpg')
    pil_image = logic.return_random_pil_image()
    pil_image.save(response, 'png')
    return response
