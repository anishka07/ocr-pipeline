import shutil
import uuid

from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse

from app.core.ocr_processor import OCRProcessor
from app.models.document import DocumentType
from app.models.request import OCRType
from app.utils.settings import PathSettings

router = APIRouter()


@router.post("/extract/")
async def extract_data(
    file: UploadFile = File(...),
    document_type: str = Form(...),
    ocr_type: OCRType = Form(...)
):
    # Save uploaded file
    temp_filename = f"{uuid.uuid4()}.pdf"
    temp_file_save_path = PathSettings.TEMP_FILE_DIR / temp_filename
    with open(temp_file_save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    processor = OCRProcessor(pdf_name=temp_filename)
    document_info = processor.process_with_factory(
        document_type=DocumentType(document_type),
        ocr_type=ocr_type
    )

    temp_file_save_path.unlink(missing_ok=True)

    return JSONResponse(
        content={"fields": [field.dict() for field in document_info.fields]}
    )
