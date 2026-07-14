import os
import pytesseract
from pdf2image import convert_from_path

from app.core.preprocessor import preprocess_image

# Tesseract Path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Poppler Path
POPPLER_PATH = r"C:\Users\PMYLS\OneDrive\Desktop\Alina\Release-26.02.0-0\poppler-26.02.0\Library\bin"


def extract_text(file_path):

    extension = os.path.splitext(file_path)[1].lower()

    # If uploaded file is PDF
    if extension == ".pdf":

        pages = convert_from_path(
            file_path,
            poppler_path=POPPLER_PATH
        )

        temp_image = "uploads/temp_page.png"

        pages[0].save(temp_image, "PNG")

        processed_image = preprocess_image(temp_image)

    else:
        processed_image = preprocess_image(file_path)

    extracted_text = pytesseract.image_to_string(processed_image)

    return extracted_text