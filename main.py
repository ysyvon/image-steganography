import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image
import numpy as np

def text_to_binary(message):
    """ Convert text to binary. """
    return ''.join(format(ord(char), '08b') for char in message)

def binary_to_text(binary):
    """ Convert binary to text. """
    return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))

def encode_image(img, message):
    """ Encode a message into an image using the LSB of each pixel. """
    binary_message = text_to_binary(message) + '1111111111111110'  # Delimiter
    pixels = np.array(img)
    flat_pixels = pixels.flatten()

    if len(binary_message) > len(flat_pixels):
        raise ValueError("The message is too long to fit in the image.")

    for i, bit in enumerate(binary_message):
        flat_pixels[i] = (flat_pixels[i] & ~1) | int(bit)

    return Image.fromarray(flat_pixels.reshape(pixels.shape), 'RGBA')

def decode_image(img):
    """ Decode a message from an image by reading the LSB of each pixel. """
    pixels = np.array(img)
    flat_pixels = pixels.flatten()

    binary_message = ''.join([str(pixel & 1) for pixel in flat_pixels])
    delimiter = binary_message.find('1111111111111110')

    if delimiter != -1:
        binary_message = binary_message[:delimiter]
        return binary_to_text(binary_message)
    return "No message found."

def load_image():
    """ Open a file dialog to select an image. """
    return filedialog.askopenfilename()

def save_image(img):
    """ Open a file dialog to save an image. """
    file_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[('PNG files', '*.png')])
    if file_path:
        img.save(file_path, 'PNG')  # Explicitly save as PNG to support RGBA

def encode():
    img_path = load_image()
    if img_path:
        img = Image.open(img_path).convert('RGBA')
        message = simpledialog.askstring("Input", "Enter the message to encode:")
        if message:
            encoded_img = encode_image(img, message)
            save_image(encoded_img)
            messagebox.showinfo("Success", "The message has been encoded.")

def decode():
    img_path = load_image()
    if img_path:
        img = Image.open(img_path).convert('RGBA')
        message = decode_image(img)
        messagebox.showinfo("Decoded Message", message)

def main():
    root = tk.Tk()
    root.title("Image Steganography Tool")
    root.geometry("300x150")

    encode_button = tk.Button(root, text="Encode Message", command=encode)
    encode_button.pack(fill='x', expand=True)

    decode_button = tk.Button(root, text="Decode Message", command=decode)
    decode_button.pack(fill='x', expand=True)

    root.protocol("WM_DELETE_WINDOW", root.quit)  # Handle the window close event
    root.mainloop()

if __name__ == "__main__":
    main()
