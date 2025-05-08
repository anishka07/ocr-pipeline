from enum import Enum
from pydantic import BaseModel


class OCRType(str, Enum):
    tesseract = 'tesseract'
    regex = 'regex'

class OCRRequest(BaseModel):
    document_type: str
    engine_type: OCRType