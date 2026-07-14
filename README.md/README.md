# 📄 Certificate OCR System

A web-based **Certificate OCR System** developed using **FastAPI** and **Tesseract OCR**. This application allows users to upload certificate images, extract text automatically using Optical Character Recognition (OCR), display the extracted information, and download the OCR result as a text file.

---

# 🚀 Features

- Upload certificate images (JPG, JPEG, PNG)
- Extract text using Tesseract OCR
- Display uploaded certificate
- Display extracted OCR text
- Smart extraction of:
  - Student Name
  - Course
  - Date
  - Instructor
- Download OCR result as a `.txt` file
- Responsive and user-friendly interface

---

# 🛠 Technologies Used

- Python 3
- FastAPI
- HTML5
- CSS3
- Jinja2 Templates
- Pillow (PIL)
- Pytesseract
- Tesseract OCR
- Uvicorn

---

# 📁 Project Structure

```
Certificate-OCR-System
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── uploads/
│
├── main.py
├── requirements.txt
├── README.md
└── ocr_result.txt
```

---

# ⚙ Installation

## Clone the project

```bash
git clone <repository-link>
```

or download the ZIP file.

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate it.

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Tesseract OCR

Download and install:

https://github.com/UB-Mannheim/tesseract/wiki

After installation, update the path inside **main.py**

Example:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

# ▶ Run the Project

```bash
python -m uvicorn main:app --reload
```

Open your browser:

```
http://127.0.0.1:8000
```

---

# 📋 How to Use

1. Open the application.
2. Upload a certificate image.
3. Click **Upload Certificate**.
4. OCR extracts the text automatically.
5. View:
   - Uploaded certificate
   - Extracted information
   - Complete OCR text
6. Click **Download OCR Result** to save the extracted text.

---

# 📸 Screenshots

Add screenshots here before submitting.

Example:

- Home Page
- Upload Certificate
- OCR Result
- Download OCR Result

---

# 📌 Future Enhancements

- PDF certificate support
- Database integration (SQLite/MySQL)
- Export OCR result as PDF
- OCR history
- User authentication
- Certificate verification

---

# 👩‍💻 Author

**ALINA SHARIF**

Certificate OCR System

Developed using FastAPI and Tesseract OCR.

---

# 📄 License

This project is developed for educational purposes.