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

if __name__ == "__main__":
    input_image_path = "./xiya.png"
    output_image_path = "./xiya_out_move.png"
    
    add_white_background(input_image_path, output_image_path)
