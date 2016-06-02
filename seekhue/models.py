"""Models for Seek Hue: Color Quantizer web app."""

from django.db import models


class Painting(models.Model):
    """docstring for Painting model."""

    source = models.ImageField()
    seekhue_sort = models.ImageField()
    artist = models.CharField(
        max_length=80,
        default='',
    )
    title = models.CharField(
        max_length=80,
        default='',
    )
    data = models.TextField(
        default='',
    )
    timestamp = models.DateField(
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
            self.data,
        )
