# Image-Data-Generation

This project is designed to generate image datasets from text, particularly useful for creating training data for optical character recognition (OCR) or similar machine learning tasks. It provides various scripts to generate images with text in different fonts, sizes, colors, and orientations.

## Features

- Generate images from text with customizable font, size, and color
- Create datasets with rotated text
- Add noise and blur to generated images
- Process text files to create image datasets
- Support for multiple languages (currently includes Hindi font support)

## Prerequisites

- Python 3.x
- Pillow (PIL Fork)
- NumPy

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/Image-Data-Generation.git
   cd Image-Data-Generation
   ```

2. Install the required dependencies:
   ```
   pip install pillow numpy
   ```

3. Ensure you have the necessary font files in the `font/hindi` directory.

## Usage

The project includes several Python scripts for different image generation tasks:

### imgBySize.py

Generates images of text in different sizes.

```
python imgBySize.py
```

### imgByFont.py

Creates images using various fonts.

```
python imgByFont.py
```

### imgByRotation.py

Generates images with rotated text.

```
python imgByRotation.py
```

### imgByColor.py

Creates images with random background and font colors.

```
python imgByColor.py
```

### imgByNoiseandBlur.py

Generates images with added noise and blur effects.

```
python imgByNoiseandBlur.py
```

### temp3.py

Processes text files to generate images.

```
python temp3.py
```

### img2text.py

Extracts text from images (details may vary based on actual implementation).

```
python img2text.py
```

## Configuration

Each script allows for customization of various parameters such as font size, rotation angle, noise level, etc. Modify these parameters in the scripts according to your requirements.

## Output

Generated images are saved in the `output` directory, organized by the type of generation method used.

## Contributing

Contributions to improve the project are welcome. Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Thanks to all contributors who have helped with this project.
- Special thanks to the developers of Pillow and NumPy libraries.
