import json
import re

import numpy as np
from pytesseract import pytesseract

from app.models.request import OCRResponse
from app.src.base import ExtractionStrategy
from app.utils.logger import get_custom_logger
from app.utils.preprocess_pdf import PDFPreProcessor
from app.utils.response import gemini_response
from app.utils.settings import PathSettings


class TesseractExtractionStrategy(ExtractionStrategy):

    def __init__(self):
        self.logger = get_custom_logger(name="TesseractExtractionStrategy")

    def extract_from_file(self, pdf_path, dpi: int = 300) -> OCRResponse:
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
        response = re.sub(r"```(?:json)?", "", response)
        response = response.replace("```", "").strip()

        response = response.replace("None", "null")
        parsed_output = json.loads(response)
        print(parsed_output)
        output = OCRResponse(**parsed_output)

        return output


if __name__ == '__main__':
    a = TesseractExtractionStrategy()
    print(a.extract_from_file(PathSettings.PDF_DIR / "docsumo.pdf"))