
# Image Steganography Tool

This Python-based GUI application allows you to encode and decode hidden messages within images using the Least Significant Bit (LSB) steganography method. It's designed to be simple to use, with straightforward options to embed or extract text messages from PNG images.

## Features

- **Encode Text into Images**: Hide messages within images with minimal visual changes.
- **Decode Text from Images**: Extract hidden messages from images.
- **Graphical User Interface**: Easy-to-use interface, allowing for quick operations.
- **Support for PNG**: Works with PNG images to avoid compression issues that might alter the embedded message.

## Prerequisites

Before you start using the Image Steganography Tool, make sure you have the following installed:
- Python 3.x
- PIL (Pillow)
- NumPy
- Tkinter (usually included with Python)

## Installation

1. **Clone the repository or download the ZIP**:
   ```bash
   git clone https://your-repository-url.git
   ```
   or download and extract the ZIP file.

2. **Install dependencies**:
   If not already installed, you'll need to install the Pillow and NumPy libraries. This can be done via pip:
   ```bash
   pip install pillow numpy
   ```

## Usage

To run the tool, execute the script from your command line:

```bash
python main.py
```

### Encoding a Message
1. Click the `Encode Message` button.
2. Select an image file (PNG).
3. Enter the message you wish to encode when prompted.
4. Choose where to save the encoded image.

### Decoding a Message
1. Click the `Decode Message` button.
2. Select an image file with a hidden message.
3. The decoded message will be displayed if any message is found.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request.

## License

MIT License

## Contact

Ys - 121690001+ysyvon@users.noreply.github.com

Project Link: https://github.com/ysyvon/image-steganography
