from app.models.document import DocumentType
from app.models.request import OCRType
from app.src.base import ExtractionStrategy
from app.src.tesseract_text_extractor import TesseractExtractionStrategy
from app.src.easy_ocr_extractor import EasyOCRExtractionStrategy


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
                return EasyOCRExtractionStrategy()

        raise ValueError("Invalid engine type or document type combination.")
