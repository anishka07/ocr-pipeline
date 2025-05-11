from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class OCRType(str, Enum):
    tesseract = 'tesseract'
    easyocr = 'easyocr'

class OCRRequest(BaseModel):
    document_type: str
    engine_type: OCRType


class OCRResponse(BaseModel):
    Name: Optional[str] = Field(None, alias="Name")
    College: Optional[str] = Field(None, alias="College")
    Federal_Tax_Classification: Optional[str] = Field(None, alias="Federal Tax Classification")
    Exempt_payee_code: Optional[str] = Field(None, alias="Exempt payee code")
    FATCA_reporting_code: Optional[str] = Field(None, alias="FATCA reporting code")
    Address: Optional[str] = Field(None, alias="Address")
    city_state_zip: Optional[str] = Field(None, alias="city_state_zip")
    social_security_number: Optional[str] = Field(None, alias="social_security_number")
    employer_identification: Optional[str] = Field(None, alias="employer_identification")