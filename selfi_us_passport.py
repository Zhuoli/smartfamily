import cv2
from rembg import remove
from PIL import Image
from io import BytesIO
import numpy as np

def make_background_white(image_path, output_path):
    # Read the input image data
    with open(image_path, "rb") as f:
        input_image_data = f.read()

    # Remove the background from the input image
    img_without_bg = remove(input_image_data)
    
    # Convert the image with removed background to a PIL.Image object
    img_no_bg_pil = Image.open(BytesIO(img_without_bg))

    # Convert the PIL.Image object to a NumPy array
    img_no_bg_np = np.array(img_no_bg_pil)

    # Apply a threshold to the alpha channel
    alpha_threshold = 50
    img_no_bg_np[:, :, 3] = np.where(img_no_bg_np[:, :, 3] > alpha_threshold, 255, 0)

    # Convert the NumPy array back to a PIL.Image object
    img_no_bg_pil = Image.fromarray(img_no_bg_np)

    # Create a white background image with the same size
    white_background = Image.new("RGBA", img_no_bg_pil.size, "WHITE")
    
    # Paste the image without background on the white background using its alpha channel as a mask
    white_background.paste(img_no_bg_pil, mask=img_no_bg_pil.split()[3]) # Alpha channel is the 4th channel
    
    # Convert the image to RGB mode (removes alpha channel)
    white_background = white_background.convert("RGB")
    
    # Save the image with white background
    white_background.save(output_path)
from PIL import Image

def add_white_background(input_path, output_path):
    # Open the input image as a PIL.Image object
    input_image = Image.open(input_path)

    # Calculate the desired head height ratio (50%-69%)
    desired_head_height_ratio = 0.6  # Adjust this value between 0.5 and 0.69 as needed

    # Calculate the dimensions of the new image based on the desired head height ratio
    width, height = input_image.size
    new_image_height = int(height / desired_head_height_ratio)

    # Create a new image with a plain-white background
    white_background = Image.new("RGBA", (width, new_image_height), "WHITE")

    # Calculate the y-coordinate at which to paste the original image
    paste_y = int((new_image_height - height) * 0.7)  # Adjust this value to position the head correctly

    # Paste the original image onto the new image with the plain-white background
    white_background.paste(input_image, (0, paste_y))

    # Save the adjusted image
    white_background.save(output_path, format="PNG")


'''
This code creates a new 4x6 inch image with a plain-white background and pastes your 2x2 inch photo onto it. 
The dpi variable sets the resolution of the output image in dots per inch. 
The paste_x and paste_y variables determine the position at which to paste the 2x2 inch photo onto the 4x6 
inch photo paper, centering the photo in this case.
'''
def create_printable_image_grid(input_path, output_path, dpi=300):
    # Open the input image as a PIL.Image object
    input_image = Image.open(input_path)

    # Set the DPI and calculate the dimensions of the 4x6 inch photo paper in pixels
    photo_paper_width = int(4 * dpi)
    photo_paper_height = int(6 * dpi)

    # Calculate the number of 2x2 inch photos that can fit in a row and a column
    num_photos_row = photo_paper_width // input_image.width
    num_photos_col = photo_paper_height // input_image.height

    # Create a new image with a plain-white background
    photo_paper = Image.new("RGBA", (photo_paper_width, photo_paper_height), "WHITE")

    # Paste the 2x2 inch photos onto the 4x6 inch photo paper in a grid
    for row in range(num_photos_row):
        for col in range(num_photos_col):
            paste_x = row * input_image.width
            paste_y = col * input_image.height
            photo_paper.paste(input_image, (paste_x, paste_y))

    # Save the adjusted image
    photo_paper.save(output_path, format="PNG")

if __name__ == "__main__":
    input_image_path = "./tutu.jpeg"
    output_image_path = "./tutu_us_passport.png"

    #add_white_background(input_image_path, output_image_path)
    create_printable_image_grid(input_image_path, output_image_path)