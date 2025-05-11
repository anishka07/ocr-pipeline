from enum import Enum


class DocumentType(str, Enum):
    OCR = None
    W9 = "w9"
    W2 = "w2"  # Prepared for future extension
    INVOICE = "invoice"  # Prepared for future extension
    GENERIC = "generic"  # Fallback for unknown document types
