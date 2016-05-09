The Color Quantizer

**Name**

Colorist (ColorList), **Huey** ("Hue"-lia Louise Dreyfus)
*SeekHue ('CQ')*


**High-level Product**

This web app will take image files, deconstruct them, analyze the pixel color values, and reorder these values into a "hue-map": a representation of existing colors sorted into hexadecimal order.


**Specific Functionality**

*Main Page*

The main page will feature an upload bar that accepts a few file formats. Below the upload bar will be a small gallery of populated from our data base of past transformations.

Once a user has hit submit, a new window will appear showing the original image as well as the hue-map side-by-side. The upload bar will appear above the new window for future uploads. The original image as well as hue-map will be created using JavaScript objects.


**Data Model**

1. Image:
Each image will represent the source file submitted by a user or uploaded for testing/development of the app.

They will contain:
*Unique ID*
*Color Analysis*
  Statistics:
    Which hues are present (rgb translated to hexadecimal)?
    How many pixels of each hue are there?
*Hue-Map Data*
  A sorted, array-like object that reorders the pixel color array created in image processing.


**Technical Components**

Images will be submitted on our HTML/CSS/JavaScript enabled Front-end. The image source, as a file or url, will be passed through JavaScript validation tests to prevent malicious code or unsupported file types.

The image source will pass through the Django powered framework to the processing program and database.

When each new image enters the database it will be assigned a unique ID and be converted into an Image object from the Pillow module to allow for color analysis and sorting with Image object methods.

A separate Python module will take pixel/color data and sort/reconstruct it into the appropriate data type for visualization.

The newly sorted, array-like color pixel list will be sent back to the web app to be visualized in JavaScript exploring the D3 library.


**Schedule**

1. Python Image Modules to deconstruct, analyze, and reconstruct color data - medium - 3 days
2. Image and analysis database - medium - 2 days
3. HTML/CSS/JavaScript/jQuery - medium - 2 days
4. Web Framework (Django) - difficult(?) - 2 days
5. Javascript visualizations - medium - 3 days


**Further Work**

*Additional Functionality*

1. User Sign-In / Profile Page

Allow users to view their past uploads and most frequently document pixel colors.

2. Palette Library

I plan on testing my image software on paintings. If Google Art Project or other public repositories can serve as a friendly API, I will work on further developing my database by creating Artist objects that save and categorize images by artist and date.

*Pie-in-the-sky Ambitions*

If I am able to complete the basic parameters of my MVP and the aforementioned user profile/artist library systems, I want to attempt to implement a simple learning algorithm that will analyze the most frequently used colors of user profiles and cross reference these favorites with the global correlations of certain colors in the database.

If user x likes specific hues of green, and there is a strong correlation of other users enjoying that hue and a specific hue of red, I want to recommend the red hue to user x.
