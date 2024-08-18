import sys
import pytesseract
from PIL import Image

# Ensure the Tesseract-OCR executable is accessible
# Uncomment and update the line below if Tesseract is not in your PATH
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text(image_path):
    try:
        # Open the image file
        img = Image.open(image_path)
        
        # Use pytesseract to do OCR on the image
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