import uvicorn
from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(title="OCR Extraction API")
app.include_router(router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)