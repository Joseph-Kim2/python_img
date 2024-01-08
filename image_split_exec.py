# -*- coding: utf-8 -*-
from images import Image  # Assuming you have an 'images' module that provides the Image class
import image_split_mod as sm  # Assuming you have an 'image_split_mod' module with the split function

def main():
    # Get the name of the image file from the user
    pic_name = input("Give the name of the file (include .gif at the end):")

    # Create an Image object from the specified file
    image1 = Image(pic_name)

    # Call the split function from the 'image_split_mod' module
    # Note: Ensure that the 'split' function returns two images, or adjust accordingly.
    image1, image2 = sm.split(image1)

    # Display the two halves of the image
    print("Displaying the original image:")
    image1.draw()

    print("\nDisplaying the split image:")
    image2.draw()

if __name__ == "__main__":
    main()