import os
from PIL import Image, ImageDraw, ImageFont

def generate_image_by_size(text, font_path, font_size):
    # Load the font
    font = ImageFont.truetype(font_path, font_size)

    # Get the mask for the text
    mask = font.getmask(text)

    # Get the size of the text bounding box
    text_bbox = mask.getbbox()

    # Calculate text dimensions with descent
    text_width = text_bbox[2] - text_bbox[0]
    descent = font.getmetrics()[-1]  # Get descent value
    text_height = text_bbox[3] - text_bbox[1] + descent

    # Create a new image with white background
    image = Image.new("RGB", (text_width + 20, text_height + 20), color="white")
    draw = ImageDraw.Draw(image)

    # Calculate text position
    x = (image.width - text_width) / 2 - text_bbox[0]
    y = (image.height - text_height) / 2 - text_bbox[1]

    # Draw the text on the image
    draw.text((x, y), text, font=font, fill="black")

    return image

def generate_images_for_fonts(word, font_directory, font_sizes, output_directory):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # List all font files in the directory
    font_files = os.listdir(font_directory)
    for font_file in font_files:
        if font_file.endswith(".ttf"):
            font_path = os.path.join(font_directory, font_file)
            font_name = os.path.splitext(font_file)[0]
            print(f"Generating images using font: {font_name}")
            for font_size in font_sizes:
                # Generate image for each font size
                image = generate_image_by_size(word, font_path, font_size)
                output_filename = os.path.join(output_directory, f"{word}_{font_name}_size_{font_size}.jpg")
                image.save(output_filename)

# Example usage:
word = input("Enter the word: ")
font_directory = "font/hindi"
font_sizes = [24, 36, 48]  # Set the desired font sizes
output_directory = 'output/hindi/ByFont'

generate_images_for_fonts(word, font_directory, font_sizes, output_directory)
print("Images generated successfully.")
