"""Models for Seek Hue: Color Quantizer web app."""

import uuid

from django.db import models


def unique_file_name(_, filename):
    """."""
    random_prefix = str(uuid.uuid4()) + '_'
    return random_prefix + filename


class Painting(models.Model):
    """docstring for Painting model."""

    source = models.ImageField(upload_to=unique_file_name)
    seekhue_sort = models.ImageField(upload_to=unique_file_name)
    artist = models.CharField(
        max_length=80,
        default='',
    )
    title = models.CharField(
        max_length=80,
        default='',
    )
    year = models.CharField(
        max_length=4,
        default='',
    )
    data = models.TextField(
        default='',
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        """Magic string displaying painting artist and title."""
        return '{!r}, {!r}'.format(
            self.artist,
            self.title,
        )

    def __repr__(self):
        """Magic repr displaying image source."""
        return 'Painting(Source:{!r}, Seekhue Sort:{!r}, Artist:{!r}, Title:{!r}, Data:{!r})'.format(
            self.source,
            self.seekhue_sort,
            self.artist,
            self.title,
            self.year,
            self.data,
        )
