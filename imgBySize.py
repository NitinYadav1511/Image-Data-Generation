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

def generate_image_for_word(word, font_path, font_sizes, output_directory):
  # Create output directory if it doesn't exist
  if not os.path.exists(output_directory):
    os.makedirs(output_directory)
  
  for font_size in font_sizes:
    # Generate image for each font size
    image = generate_image_by_size(word, font_path, font_size)
    output_filename = os.path.join(output_directory, f"{word}_size_{font_size}.jpg")
    image.save(output_filename)

# Example usage:
word = input("Enter the word: ")
font_path = "font/hindi/Jaldi-Bold.ttf"
font_sizes = [int(size) for size in input("Enter font sizes separated by space: ").split()]  # e.g., "24 36 48"
output_directory = 'output/hindi/BySize'

generate_image_for_word(word, font_path, font_sizes, output_directory)
print("Images generated successfully.")
