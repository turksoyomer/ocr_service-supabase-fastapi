# OCR Service with Supabase & FastAPI

A simple file upload and OCR (Optical Character Recognition) service built with FastAPI and Supabase. Supports image uploads and text extraction using Tesseract.

---

## Features
- Upload images for OCR
- Extract text from images using Tesseract
- Supabase integration (coming soon)

## Installation

### Python & Dependencies
```bash
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Tesseract Installation
- **Ubuntu/Debian**:
  ```bash
  sudo apt install -y tesseract-ocr
  ```
- **macOS**:
  ```bash
  brew install tesseract
  brew install tesseract-lang # for language support
  ```

## Usage

Start the FastAPI server:
```bash
uvicorn main:app --reload
```

## Next Steps
- Supabase integration
