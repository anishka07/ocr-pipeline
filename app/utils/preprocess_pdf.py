from pathlib import Path

import cv2
from pdf2image import convert_from_path

from app.utils.logger import get_custom_logger


class PDFPreProcessor:

    def __init__(self, pdf_path: Path, dpi: int = 300):
        self.dpi = dpi
        self.pdf_path = pdf_path
        self.logger = get_custom_logger(name="PDFPreProcessor")
        
    def convert_pdf_to_images(self):
        self.logger.info(f"Converting PDF to images at {self.dpi} dpi.")
        return convert_from_path(self.pdf_path, dpi=self.dpi)

    def remove_lines(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        binary = cv2.adaptiveThreshold(~gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY, 15, -2)
        # Detect horizontal lines
        horizontal = binary.copy()
        h_size = horizontal.shape[1] // 30
        h_structure = cv2.getStructuringElement(cv2.MORPH_RECT, (h_size, 1))
        horizontal = cv2.erode(horizontal, h_structure)
        horizontal = cv2.dilate(horizontal, h_structure)
        # Detect vertical lines
        vertical = binary.copy()
        v_size = vertical.shape[0] // 30
        v_structure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, v_size))
        vertical = cv2.erode(vertical, v_structure)
        vertical = cv2.dilate(vertical, v_structure)
        # Combine both
        mask = cv2.add(horizontal, vertical)
        cleaned = cv2.bitwise_and(binary, binary, mask=cv2.bitwise_not(mask))

        cleaned_final = cv2.bitwise_not(cleaned)
        # Inpaint original image for color restoration
        inpainted = cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)
        return cleaned_final, inpainted


