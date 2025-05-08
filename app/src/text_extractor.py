import numpy as np
from pytesseract import pytesseract

from app.models.document import DocumentInfo, DocumentField
from app.src.base import ExtractionStrategy
from app.utils.logger import get_custom_logger
from app.utils.preprocess_pdf import PDFPreProcessor
from app.utils.response import gemini_response


class OCRExtractionStrategy(ExtractionStrategy):

    def __init__(self):
        self.logger = get_custom_logger(name="OCRExtractionStrategy")

    def extract_from_file(self, pdf_path, dpi: int = 300) -> DocumentInfo:
        preprocessor = PDFPreProcessor(pdf_path=pdf_path, dpi=dpi)
        pages = preprocessor.convert_pdf_to_images()

        all_text = []
        for i, page in enumerate(pages):
            image = np.array(page)
            image = image[:, :, ::-1]  # RGB to BGR for OpenCV

            cleaned_binary, _ = preprocessor.remove_lines(image)
            page_text = pytesseract.image_to_string(cleaned_binary)
            self.logger.info(f"Extracted text from page {i + 1}")
            all_text.append(page_text)

        full_text = " ".join(all_text).replace("v|", "[*]")
        response = gemini_response(context=full_text)

        fields = [
            DocumentField(name=key, value=value)
            for key, value in response.items()
        ]
        return DocumentInfo(fields=fields)

