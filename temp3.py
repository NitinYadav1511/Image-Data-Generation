import os
from PIL import Image, ImageDraw, ImageFont

def generate_image_by_size(text, font_path, font_size):
    # Load the font
    font = ImageFont.truetype(font_path, font_size)

    # Get the mask for the text
    mask = font.getmask(text)

    # Get the size of the text bounding box
    text_bbox = mask.getbbox()

    # Calculate the size of the image
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Create a new image with white background
    image = Image.new("RGB", (text_width + 10, text_height + 10), color="white")
    draw = ImageDraw.Draw(image)

    # Calculate text position
    x = (image.width - text_width) / 2 - text_bbox[0]
    y = (image.height - text_height) / 2 - text_bbox[1]

    # Draw the text on the image
    draw.text((x, y), text, font=font, fill="black")

    return image



def process_text_files(directory_path, output_directory, font_path, font_size, words_limit=1000):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # List all files in the directory
    files = os.listdir(directory_path)
    for file_name in files:
        if file_name.endswith(".txt"):
            file_path = os.path.join(directory_path, file_name)
            output_subdirectory = os.path.join(output_directory, file_name[:-4])
            # Create subdirectory for each text file
            if not os.path.exists(output_subdirectory):
                os.makedirs(output_subdirectory)
            
            with open(file_path, 'r', encoding='utf-8') as file:
                word_count = 0
                for line in file:
                    # Split line into words
                    words = line.strip().split()
                    for word in words:
                        if word_count < words_limit:
                            # Generate image for each word
                            image = generate_image_by_size(word, font_path, font_size)
                            i = 0
                            # Save images with incrementing index
                            while True:
                                output_filename = os.path.join(output_subdirectory, f"image_{i}.jpg")
                                if not os.path.exists(output_filename):
                                    break
                                i += 1
                            image.save(output_filename)
                            word_count += 1
                        else:
                            break  # Stop processing words if word limit reached
                        
# Example usage:
input_directory = 'text/hindi'
output_directory = 'output/hindi'
font_path = "font/hindi/Jaldi-Bold.ttf"
font_size = int(input("Enter the font size: "))  # e.g., 24

process_text_files(input_directory, output_directory, font_path, font_size)
print("######################################################################")