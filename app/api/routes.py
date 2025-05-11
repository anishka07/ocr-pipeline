import json
from pathlib import Path
from tempfile import NamedTemporaryFile

from fastapi import APIRouter, UploadFile, File, Form, status
from fastapi.responses import JSONResponse

from app.core.ocr_processor import OCRProcessor
from app.models.document import DocumentType
from app.models.request import OCRType, ExtractionResult
from app.utils.logger import get_custom_logger
from app.utils.response import gemini_response

router = APIRouter()

logger = get_custom_logger(__name__)


@router.get("/")
async def root():
    return {"message": "Welcome to the OCR Extraction API"}


@router.get("/health")
async def health_check():
    return {"status": "ok"}


@router.post("/extract/")
async def extract_data(
    file: UploadFile = File(...),
    document_type: DocumentType = DocumentType.W9,
    ocr_type: OCRType = OCRType.tesseract,
) -> ExtractionResult:
    try:
        suffix = Path(file.filename).suffix if file.filename else ".pdf"
        with NamedTemporaryFile(delete=True, suffix=suffix) as temp_file:
            contents = await file.read()
            temp_file.write(contents)
            temp_path = temp_file.name

            processor = OCRProcessor(pdf_name=temp_path)
            ocr_info = processor.process_with_factory(
                document_type=document_type, ocr_type=ocr_type
            )
            document_info = gemini_response(
                context=ocr_info, schema=ExtractionResult.model_json_schema()
            )

            document_info = json.loads(document_info)

        return document_info

    except Exception as e:
        logger.error(f"Error processing document: {str(e)}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"error": str(e)}
        )
