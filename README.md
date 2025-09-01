# ocr_service-supabase-fastapi
File Upload &amp; OCR Service

---
installation:
    python3.12 -m venv venv
    pip install -r requirements.txt
    for Ubuntu/Debian:
        sudo apt install -y tesseract-ocr
    for macOS:
        brew install tesseract
        brew install tesseract-lang (for language support)

run:
    uvicorn main:app --reload
