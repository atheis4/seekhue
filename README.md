# SeekHue

SeekHue takes an image file, creates a three-tuple of the image pixel color values, and sorts them by their hue, lightness, and saturation--creating a visual representation of color distribution. Visit the proposal [here](/seek_hue.md).

# Setup

After cloning this repository and setting up your virtual environment, you'll need to complete three more steps to run SeekHue:

  1. Install dependencies Pillow and Django.
  2. Run makemigrations to initialize model classes in Django database.
  3. Create a folder called media/ in app root directory--source images and transformations will be stored here.

# Usage

From the index page you can view previously completed transformations by scrolling your cursor over an original painting, or you can upload your own painting through the submit button.

Submitting an image will take you to a new page which displays your original image and its transformation.

There is also a search bar on each page that accepts basic search terms, such as a particular artist, country, or art movement.
