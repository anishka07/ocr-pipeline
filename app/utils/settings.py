from pathlib import Path


PARENT_DIR = Path(__file__).resolve().parent.parent.parent


class PathSettings:
    APP_DIR = PARENT_DIR / "app"
    PDF_DIR = PARENT_DIR / "pdfs"
    LOG_DIR = PARENT_DIR / "logs"


class Constants:
    GEMINI_PROMPT: str = """
    This is the text extracted from a PDF form:
    {}
    Extract in this format: 
    {{
        "Name": ,
        "College": ,
        "Federal Tax Classification": ,
        "Exempt payee code": ,
        "FATCA reporting code": ,
        "Address": ,
        "city_state_zip": ,
        "social_security_number": ,
        "employer_identification": ,
    }}
    If any are missing, fill the field with None
    """
