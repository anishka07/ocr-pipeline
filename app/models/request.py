from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class OCRType(str, Enum):
    tesseract = "tesseract"
    easyocr = "easyocr"


class ExtractionResult(BaseModel):
    name: Optional[str] = Field(
        None, description="Full name of the individual or entity"
    )
    college: Optional[str] = Field(
        None, description="Name of the college or educational institution"
    )
    # requestor_name: Optional[str] = Field(None, description="Full name of the requestor")
    federal_tax_classification: Optional[str] = Field(
        None,
        description="Federal tax classification (e.g., Individual, Corporation, etc.)",
    )
    exempt_payee_code: Optional[str] = Field(
        None, description="Exempt payee code if applicable"
    )
    fatca_reporting_code: Optional[str] = Field(
        None, description="FATCA reporting code if applicable"
    )
    address: Optional[str] = Field(
        None, description="Street address of the individual or entity"
    )
    city_state_zip: Optional[str] = Field(
        None, description="City, state, and ZIP code combined"
    )
    social_security_number: Optional[str] = Field(
        None, description="Social Security Number (SSN), if provided"
    )
    employer_identification_number: Optional[str] = Field(
        None,
        description="Employer Identification Number (EIN), if provided.",
    )

    @field_validator("employer_identification_number")
    def clean_ein(cls, v: Optional[str]) -> Optional[str]:
        if not v:
            return None
        digits_only = "".join(c for c in v if c.isdigit())
        return digits_only

    """
    Example:
    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "address": "123 Main Street",
                "city_state_zip": "Anytown, CA 12345",
                "employer_identification_number": "123456789",
            }
    }"""
