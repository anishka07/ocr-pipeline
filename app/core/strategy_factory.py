from app.models.document import DocumentType
from app.models.request import OCRType
from app.src.base import OCRStrategy
from app.src.tesseract_text_extractor import TesseractExtractionStrategy
from app.src.easyocr_text_extractor import EasyOCRExtractionStrategy


class ExtractionStrategyFactory:
    def get_strategy(
        self,
        document_type: DocumentType,
        ocr_type: OCRType,
    ) -> OCRStrategy:
        if document_type == DocumentType.W9:
            if ocr_type == OCRType.tesseract:
                return TesseractExtractionStrategy()
            elif ocr_type == OCRType.easyocr:
                return EasyOCRExtractionStrategy()

        raise ValueError("Invalid engine type or document type combination.")
