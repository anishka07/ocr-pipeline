import os
import shutil
import tempfile

from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse

from app.core.ocr_processor import OCRProcessor
from app.models.document import DocumentType
from app.models.request import OCRType

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Welcome to the OCR Extraction API"}


@router.get("/health")
async def health_check():
    return {"status": "ok"}


@router.post("/extract/")
async def extract_data(
        file: UploadFile = File(...),
        document_type: DocumentType = Form(...),
        ocr_type: OCRType = Form(...)
):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            shutil.copyfileobj(file.file, tmp)
            temp_filename = tmp.name
        await file.close()

        processor = OCRProcessor(pdf_name=temp_filename)
        document_info = processor.process_with_factory(
            document_type=document_type,
            ocr_type=ocr_type
        )

        return JSONResponse(content={"Field_data": document_info.dict()})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    finally:
        try:
            if temp_filename and os.path.exists(temp_filename):
                os.remove(temp_filename)
        except Exception:
            pass
