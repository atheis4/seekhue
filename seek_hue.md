The Color Quantizer


**Name**

Colorist (ColorList), **Huey** ("Hue"-lia Louise Dreyfus)
*SeekHue ('CQ')*


**High-level Product**

This web app allows users to submit their images and have them converted into a "hue-map": the reordering of pixels into hexadecimal order.

Users can build a profile and follow their progression of their color style through changing seasons or analyze the colors of their favorite artists.


**Specific Functionality**

The web app will have a simple interface that allows users to (1.) create a profile, (2.) submit images to deconstruct--into a hue-map or color wheel analysis--or (3.) browse our collection of color profiles from the community, art history, movies, fashion, or time periods. Users can also (4.) share their profiles, favorite colors, and recent image transformations to their social media.

1. A user's profile will consist of a personalized color wheel. This wheel will update over time to reflect the colors they have uploaded or bookmarked.

User's will also be able to display their color uploads in sequential order, search past color trends, and become more familiar with the colors in their fashion, their pictures, or their artwork.

2. The primary feature is the 'de-constructor' itself. User's will be able to submit images which are broken down by pixels, analyzed, and returned as an image of the gradient map or color wheel.

3. There will be a database of color profiles for users to peruse. Users can search for specific artists and view their most used colors as well as the progression of their color choices through time.

4. Finally, the color profile will be sharable across all social media platforms, integrated into CSS style sheets, or returned as hex, RGB, and CMYK hexcode.


**Technical Components**

Our database will store user profiles. Queries will be available to search by individual users, or any number of parameters such as time-period, genre, or discipline.

All analyzing of colors in user profiles will be done using statistics modules in Python.

Python will also be used to create the modules that analyze user submitted images by studying the average hue density over a small pixel area. I plan on implementing a multi-class classification algorithm and train it to identify the mean hue over a given pixel size expressed in hexadecimal notation. I will create and cross-validate a data set of monochromatic color samples and slowly refine the algorithm until it can identify larger and more diverse color samples.

Scikit-Learn offers a multitude of objects that serve as classifiers and refiners to aid in constructing learning algorithms. I will also investigate a number of open source, optical algorithms to utilize relevant modules and structures--via ColorTag (APICloud) and Image Color Extraction (Nijikokun) APIs.

Hue density information will be mapped onto a data structure in Python and visualized on our site as a hexadecimal gradient map, 'hue-map', or the frequency of colors can be mapped on a color wheel using Javascript.


**Timeline**

The largest challenge will be constructing the learning algorithm and refining its categorization abilities through multiple training and testing sets.

The second most challenging aspect will be constructing the database and query parameters. I hope to give users a dynamic search function that can aid them in selecting colors from all sorts of inspirations and uses.

I will set aside three weeks to develop the algorithm and construct the database search functions.

The remaining week will be used to construct the site and refine the visual language of the color information and the user profile.



**Programmer's Note**

Even as I write this I recognize I have no idea what I am in store for. I have set some lofty goals and I hope that my minimal feature set is minimal enough to allow me room for error as I try to solve my engineering problem.
