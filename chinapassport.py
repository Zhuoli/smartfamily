from PIL import Image


# Adjust the DPI constant if the printer you're using has a different DPI (dots per inch). The conversion factor 25.4 is used to convert from millimeters to inches. The result will be a 4x6 inch canvas with the given picture centered at 33mm x 48mm.

def process_image_for_print(input_path, output_path):
    # Constants
    DPI = 300  # Typical DPI for printing is 300
    CANVAS_WIDTH_INCH, CANVAS_HEIGHT_INCH = 4, 6
    IMAGE_WIDTH_MM, IMAGE_HEIGHT_MM = 33, 48
    CANVAS_WIDTH_PX = CANVAS_WIDTH_INCH * DPI
    CANVAS_HEIGHT_PX = CANVAS_HEIGHT_INCH * DPI
    IMAGE_WIDTH_PX = int(IMAGE_WIDTH_MM * DPI / 25.4)
    IMAGE_HEIGHT_PX = int(IMAGE_HEIGHT_MM * DPI / 25.4)

    # Open the image and resize it
    image = Image.open(input_path)
    image = image.resize((IMAGE_WIDTH_PX, IMAGE_HEIGHT_PX), Image.LANCZOS)

    # Create a blank white canvas``
    canvas = Image.new('RGB', (CANVAS_WIDTH_PX, CANVAS_HEIGHT_PX), 'white')

    # Calculate the position to paste the image on the canvas
    paste_x = (CANVAS_WIDTH_PX - IMAGE_WIDTH_PX) // 2
    paste_y = (CANVAS_HEIGHT_PX - IMAGE_HEIGHT_PX) // 2

    # Paste the image
    canvas.paste(image, (paste_x, paste_y))

    # Save the result
    canvas.save(output_path, 'JPEG', quality=95)


def replicate_image_for_print(input_path, output_path):
    # Constants
    DPI = 300  # Typical DPI for printing is 300
    CANVAS_WIDTH_INCH, CANVAS_HEIGHT_INCH = 4, 6
    IMAGE_WIDTH_MM, IMAGE_HEIGHT_MM = 50.8, 50.8
    CANVAS_WIDTH_PX = CANVAS_WIDTH_INCH * DPI
    CANVAS_HEIGHT_PX = CANVAS_HEIGHT_INCH * DPI

    # Open the image
    image = Image.open(input_path)

    # Calculate the scaling factors for width and height
    width_scale = IMAGE_WIDTH_MM / 25.4 * DPI / image.width
    height_scale = IMAGE_HEIGHT_MM / 25.4 * DPI / image.height

    # Use the smaller scaling factor to ensure the image fits within the desired dimensions
    scale_factor = min(width_scale, height_scale)

    # Calculate the new dimensions preserving the aspect ratio
    new_width = int(image.width * scale_factor)
    new_height = int(image.height * scale_factor)
    image = image.resize((new_width, new_height), Image.ANTIALIAS)

    # Number of images that fit in width and height
    IMAGES_PER_ROW = CANVAS_WIDTH_PX // new_width
    IMAGES_PER_COLUMN = CANVAS_HEIGHT_PX // new_height

    # Create a blank white canvas
    canvas = Image.new('RGB', (CANVAS_WIDTH_PX, CANVAS_HEIGHT_PX), 'white')
    
    # Paste the images
    for i in range(IMAGES_PER_ROW):
        for j in range(IMAGES_PER_COLUMN):
            paste_x = i * new_width
            paste_y = j * new_height
            canvas.paste(image, (paste_x, paste_y))

    # Save the result
    canvas.save(output_path, 'JPEG', quality=95)

def rotate_image(input_path, degree, output_path):
    # Open the image
    image = Image.open(input_path)
    
    # Rotate the image and fill the background with white
    rotated_image = image.rotate(-degree, expand=True, fillcolor='white')  # Negative degrees to rotate in the expected direction
    
    # Save the rotated image
    rotated_image.save(output_path)

# Example usage:
replicate_image_for_print('tutu.jpeg', 'tutu_out.jpeg')
