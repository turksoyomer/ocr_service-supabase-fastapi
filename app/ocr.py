import io

import pytesseract
from PIL import Image


def extract_text_from_image(file_bytes: bytes, lang: str = "eng") -> str:
    if not check_language(lang):
        raise ValueError(f"Unsupported language: {lang}")

    image = Image.open(io.BytesIO(file_bytes))
    text = pytesseract.image_to_string(image, lang=lang)
    return text.strip()


def check_language(lang: str) -> bool:
    return lang in pytesseract.get_languages()
