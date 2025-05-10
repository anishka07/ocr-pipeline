from abc import ABC, abstractmethod

from app.models.document import DocumentInfo


class ExtractionStrategy(ABC):

    @abstractmethod
    def extract_from_file(self, pdf_path, dpi: int = 300) -> DocumentInfo:
        raise NotImplementedError("This strategy doesn't support file-based OCR extraction.")

