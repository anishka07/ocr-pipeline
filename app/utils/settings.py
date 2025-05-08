from pathlib import Path


PARENT_DIR = Path(__file__).resolve().parent.parent.parent


class PathSettings:
    APP_DIR = PARENT_DIR / "app"
    PDF_DIR = PARENT_DIR / "pdfs"
    LOG_DIR = PARENT_DIR / "logs"
    TEMP_FILE_DIR = PARENT_DIR / "temp"


class Constants:
    GEMINI_PROMPT: str = "This is the content from a w9 form: {}, i want you to extract all the relevant field values from this form and return them in a json format. Don't add any extra logic to your response."