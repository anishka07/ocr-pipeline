from abc import ABC, abstractmethod

from app.models.request import OCRResponse


class ExtractionStrategy(ABC):

    @abstractmethod
    def extract_from_file(self, pdf_path, dpi: int = 300) -> OCRResponse:
        raise NotImplementedError("This strategy doesn't support file-based OCR extraction.")

