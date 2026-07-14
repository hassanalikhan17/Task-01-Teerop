import os

import pytesseract
from pdf2image import convert_from_path

from app.core.preprocessor import preprocess_image

# Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Poppler binary location
POPPLER_PATH = (
    r"C:\Users\PMYLS\OneDrive\Desktop\Alina\Release-26.02.0-0\poppler-26.02.0\Library\bin"
)


def extract_text(file_path):

    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension == ".pdf":

        pdf_pages = convert_from_path(
            file_path,
            poppler_path=POPPLER_PATH
        )

        preview_image = "uploads/temp_page.png"

        pdf_pages[0].save(preview_image, "PNG")

        processed_image = preprocess_image(preview_image)

    else:

        processed_image = preprocess_image(file_path)

    text = pytesseract.image_to_string(processed_image)

    return text