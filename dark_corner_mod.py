
def dark_corner(image1, degree):
    """
    Darken the top-left corner of an image by reducing the RGB values of each pixel in that region.

    Parameters:
    - image1: The original image to be modified.
    - degree: The degree by which to darken the colors (0 to 255).

    Returns:
    - The modified image with the darkened top-left corner.
    """
    for y in range(image1.getHeight()):
        for x in range(image1.getWidth()):
            # Check if the pixel is in the top-left corner
            if y <= image1.getHeight() // 2 and x <= image1.getWidth() // 2:
                # Get the RGB values of the pixel
                r, g, b = image1.getPixel(x, y)

                # Darken the colors by subtracting the specified degree
                r = max(0, r - degree)
                g = max(0, g - degree)
                b = max(0, b - degree)

                # Set the modified pixel back to the image
                image1.setPixel(x, y, (r, g, b))

    # Return the modified image
    return image1