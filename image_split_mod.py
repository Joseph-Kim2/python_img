def split(image1):
    """
    Splits the input image horizontally into two halves.

    Parameters:
    - image1: The original image to be split.

    Returns:
    - Two new images representing the top and bottom halves of the original image.
    """

    # Define the color of white pixels
    white_pixel = (255, 255, 255)

    # Clone the original image
    image2 = image1.clone()  
    
    # Set the bottom half of the cloned image to white
    for y in range(image2.getHeight()):
        for x in range(image2.getWidth()):
            if y > image2.getHeight() // 2:
                image2.setPixel(x, y, white_pixel)

    # Set the top half of the original image to white
    for y in range(image1.getHeight()):
        for x in range(image1.getWidth()):
            if y <= image1.getHeight() // 2:
                image1.setPixel(x, y, white_pixel)

    # Return the modified images
    return image1, image2