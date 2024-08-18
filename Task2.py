import sys
from PIL import Image
import numpy as np

def grayscale_image(image_path):
    try:
        img = Image.open(image_path)
        img = img.convert('RGB')
        img_array = np.array(img)
        weights = np.array([0.299, 0.587, 0.114])
        grayscale_array = np.dot(img_array[...,:3], weights).astype(np.uint8)
        grayscale_img = Image.fromarray(grayscale_array)
        grayscale_img.save('C://Users/fdt/OneDrive/Desktop/JoVision AI/Images/grayscale_img.jpg')

        print("Image successfully converted and saved in Images folder")
    except Exception as e:
        return f"An error occurred: {e}"

if len(sys.argv) != 2:
    print("Usage: python text_extraction.py <image_path>")
else:
    image_path = sys.argv[1]
    grayscale_image(image_path)
