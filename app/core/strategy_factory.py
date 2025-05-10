from app.models.document import DocumentType
from app.models.request import OCRType
from app.src.base import ExtractionStrategy
from app.src.regex_extractor import RegexExtractionStrategy
from app.src.text_extractor import TesseractExtractionStrategy


class ExtractionStrategyFactory:

    def get_strategy(
            self,
            document_type: DocumentType,
            ocr_type: OCRType,
    ) ->  ExtractionStrategy:
        if document_type == DocumentType.W9:
            if ocr_type == OCRType.tesseract:
                return TesseractExtractionStrategy()
            elif ocr_type == OCRType.regex:
                return RegexExtractionStrategy()

        raise ValueError("Invalid engine type or document type combination.")
