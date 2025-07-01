from fastapi import APIRouter, UploadFile, File, HTTPException
from src.services.document_processing_service import process_pdf_and_upsert

router = APIRouter(prefix="/v1", tags=["documents"])

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """
    Upload a PDF document for processing and vector storage.
    """
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")
    
    try:
        result = await process_pdf_and_upsert(file)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing document: {str(e)}")
