import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import numpy as np

def generate_image_by_size(text, font_path, font_size, angle, bg_color):
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

    # Create a new image with background color
    image = Image.new("RGB", (text_width + 20, text_height + 20), color=bg_color)
    draw = ImageDraw.Draw(image)

    # Calculate text position
    x = (image.width - text_width) / 2 - text_bbox[0]
    y = (image.height - text_height) / 2 - text_bbox[1]

    # Draw the text on the image
    draw.text((x, y), text, font=font, fill="black")

    # Rotate the image
    rotated_image = image.rotate(angle, expand=True, fillcolor=bg_color)

    return rotated_image

def add_noise(image, noise_level):
    """
    Add random noise to the image.
    """
    img_array = np.array(image)
    noise = np.random.randint(0, noise_level + 1, img_array.shape, dtype=np.uint8)
    noisy_img_array = np.clip(img_array + noise, 0, 255)
    noisy_image = Image.fromarray(noisy_img_array)
    return noisy_image

def add_blur(image, blur_radius):
    """
    Add blur to the image.
    """
    blurred_image = image.filter(ImageFilter.GaussianBlur(radius=blur_radius))
    return blurred_image

def generate_images_for_fonts(word, font_directory, font_sizes, output_directory, max_rotation_angle, bg_color, noise_level, blur_radius):
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
                for angle in range(0, max_rotation_angle + 1):
                    # Generate image for each font size and rotation angle
                    image = generate_image_by_size(word, font_path, font_size, angle, bg_color)
                    
                    # Add noise and blur
                    noisy_image = add_noise(image, noise_level)
                    blurred_image = add_blur(noisy_image, blur_radius)
                    
                    # Save the final image
                    output_filename = os.path.join(output_directory, f"{word}_{font_name}_size_{font_size}_angle_{angle}_noise_{noise_level}_blur_{blur_radius}.jpg")
                    blurred_image.save(output_filename)

# Example usage:
word = input("Enter the word: ")
font_directory = "font/hindi"
font_sizes = [12, 24]  # Set the desired font sizes
output_directory = 'output/hindi/ByNoiseAndBlur'
max_rotation_angle = 10  # Set the maximum rotation angle(90)
bg_color = "white"  # Set the background color
noise_level = 1  # Set the noise level
blur_radius = 1  # Set the blur radius

generate_images_for_fonts(word, font_directory, font_sizes, output_directory, max_rotation_angle, bg_color, noise_level, blur_radius)
print("Images generated successfully.")
