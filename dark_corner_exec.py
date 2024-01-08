import dark_corner_mod as fm  # Assuming you have a 'dark_corner_mod' module with the dark_corner function
from images import Image  # Assuming you have an 'images' module that provides the Image class

def main():
    # Get the name of the image file from the user
    pic_name = input("Give the name of the file (include .gif at the end):")

    # Get the degree by which to darken the top-left corner from the user
    degree = int(input("Give the degree by which you will darken the top-left corner: "))

    # Create an Image object from the specified file
    image1 = Image(pic_name)

    # Call the dark_corner function from the 'dark_corner_mod' module
    # Note: Ensure that the 'dark_corner' function returns the modified image, or adjust accordingly.
    new_image = fm.dark_corner(image1, degree)

    # Display the modified image
    print("Displaying the modified image:")
    new_image.draw()

    # Save the modified image to a new file
    new_image.save("dark_top_left.gif")

if __name__ == "__main__":
    main()

