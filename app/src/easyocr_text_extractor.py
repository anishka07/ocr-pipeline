import easyocr
import numpy as np

from app.src.base import OCRStrategy
from app.utils.logger import get_custom_logger
from app.utils.preprocess_pdf import PDFPreProcessor
from app.utils.settings import PathSettings


class EasyOCRExtractionStrategy(OCRStrategy):
    def __init__(self):
        self.logger = get_custom_logger(name="EasyOCRExtractionStrategy")
        self.reader = easyocr.Reader(["en"])  # You can add more languages if needed

    def extract_from_file(self, pdf_path, dpi: int = 300) -> str:
        preprocessor = PDFPreProcessor(pdf_path=pdf_path, dpi=dpi)
        pages = preprocessor.convert_pdf_to_images()

        all_text = []
        for i, page in enumerate(pages):
            image = np.array(page)
            image = image[:, :, ::-1]  # RGB to BGR for OpenCV

            cleaned_binary, _ = preprocessor.remove_lines(image)
            result = self.reader.readtext(cleaned_binary)

            page_text = " ".join(
                [text[1] for text in result]
            )  # Join the text extracted from the image
            self.logger.info(f"Extracted text from page {i + 1}")
            all_text.append(page_text)

        full_text = " ".join(all_text).replace("v|", "[*]")
        return full_text


if __name__ == "__main__":
    a = EasyOCRExtractionStrategy()
    print(a.extract_from_file(PathSettings.PDF_DIR / "docsumo.pdf"))
