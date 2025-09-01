import shutil
import uuid
from pathlib import Path

from fastapi import FastAPI, File, Form, UploadFile

from app.ocr import extract_text_from_image

app = FastAPI()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    lang: str = Form("eng"),
):
    filename = f"{uuid.uuid4()}_{file.filename}"
    file_path = UPLOAD_DIR / filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    with open(file_path, "rb") as f:
        file_bytes = f.read()
        text = extract_text_from_image(file_bytes, lang=lang)

    return {"filename": filename, "text": text, "lang": lang}
