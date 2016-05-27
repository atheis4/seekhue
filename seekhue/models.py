"""Models for Seek Hue: Color Quantizer web app."""

from django.db import models


class Painting(models.Model):
    """docstring for Painting model."""

    source = models.ImageField()
    seekhue_sort = models.ImageField()

    def __str__(self):
        """Magic string displaying painting file source as a .jpg."""
        return '{!r}, {!r}'.format(
            self.source,
            self.seekhue_sort,
        )

    def __repr__(self):
        """Magic repr displaying image source."""
        return 'Painting(Source:{!r}, Seekhue Sort:{!r})'.format(
            self.source,
            self.seekhue_sort,
        )
