from pathlib import Path


PARENT_DIR = Path(__file__).resolve().parent.parent.parent


class PathSettings:
    APP_DIR = PARENT_DIR / "app"
    PDF_DIR = PARENT_DIR / "pdfs"
    LOG_DIR = PARENT_DIR / "logs"


class Constants:
    GEMINI_PROMPT: str = """Extract the following details from the provided PDF form text:
            {}
            
            The schema of Json should be:
            
            {}
            
            Provide the extracted data in valid JSON format with double-quoted keys and string values.
            
            If any field is missing or cannot be extracted, set its value to null.
            
            Return only the JSON object — DO NOT include any markdown formatting (no triple backticks, no extra text).
"""
