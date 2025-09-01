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

## Example

### Example Request

```bash
curl -X POST "http://127.0.0.1:8000/upload" \
     -F "file=@test.png" \
     -F "lang=tur"
```

### Example Picture

![Example OCR Image](example.png)

### Example Output

```json
{
    "filename": "495d3933-5715-4a29-829d-edaabd112b16_figure-65.png",
    "text": "It was the best of\ntimes, it was the worst\nof times, it was the age\nof wisdom, it was the\nage of foolishness...",
    "lang": "eng"
}
```

## Next Steps
- Supabase integration
