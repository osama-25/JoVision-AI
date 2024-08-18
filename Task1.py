import sys
import pytesseract
from PIL import Image

def extract_text(image_path):
    try:
        img = Image.open(image_path)
        
        text = pytesseract.image_to_string(img)
        
        return text
    except Exception as e:
        return f"An error occurred: {e}"

if len(sys.argv) != 2:
    print("Usage: python text_extraction.py <image_path>")
else:
    image_path = sys.argv[1]
    extracted_text = extract_text(image_path)
    print("Extracted Text:")
    print(extracted_text)