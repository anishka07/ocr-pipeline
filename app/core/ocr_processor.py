from app.core.strategy_factory import ExtractionStrategyFactory
from app.models.document import DocumentType, DocumentInfo
from app.models.request import OCRType
from app.utils.logger import get_custom_logger
from app.utils.settings import PathSettings


class OCRProcessor:

    def __init__(self, pdf_name: str, dpi: int = 300):
        self.logger = get_custom_logger("OCRProcessor")
        self.logger.info("OCRProcessor initialized.")
        self.pdf_name = pdf_name
        self.pdf_path = PathSettings.PDF_DIR / pdf_name
        self.dpi = dpi
        self.factory = ExtractionStrategyFactory()

    def process_with_factory(
            self,
            document_type: DocumentType,
            ocr_type: OCRType,
    ) -> DocumentInfo:
        strategy = self.factory.get_strategy(document_type, ocr_type)
        return strategy.extract_from_file(pdf_path=self.pdf_path, dpi=self.dpi)
