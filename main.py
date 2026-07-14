from fastapi import FastAPI, Request, UploadFile, File
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

import shutil
import os
import pytesseract

from app.core.ocr_engine import extract_text
from app.core.extractor import extract_information

# ==============================
# Tesseract Configuration
# ==============================

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# ==============================
# FastAPI App
# ==============================

app = FastAPI()

# ==============================
# Folder Setup
# ==============================

os.makedirs("uploads", exist_ok=True)

# ==============================
# Static Files
# ==============================

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

templates = Jinja2Templates(directory="templates")

# ==============================
# Home Page
# ==============================

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

# ==============================
# Upload Certificate
# ==============================

@app.post("/upload")
def upload_file(request: Request, file: UploadFile = File(...)):

    try:

        file_path = os.path.join("uploads", file.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        extracted_text = extract_text(file_path)

        info = extract_information(extracted_text)

        with open("ocr_result.txt", "w", encoding="utf-8") as f:
            f.write(extracted_text)

        return templates.TemplateResponse(
            request=request,
            name="result.html",
            context={
                "filename": file.filename,

                # THIS FIXES THE IMAGE
                "image": file.filename,

                # THIS DETECTS PDF / IMAGE
                "file_extension": os.path.splitext(file.filename)[1].lower(),

                "text": extracted_text,

                "name": info.get("name", ""),
                "title": info.get("title", ""),
                "organization": info.get("organization", ""),
                "date": info.get("date", ""),
                "certificate_number": info.get("certificate_number", ""),
                "grade": info.get("grade", ""),
                "duration": info.get("duration", "")
            }
        )

    except Exception as e:

        return {
            "error": str(e)
        }

# ==============================
# Download OCR Result
# ==============================

@app.get("/download")
def download_result():

    return FileResponse(
        "ocr_result.txt",
        media_type="text/plain",
        filename="OCR_Result.txt"
    )