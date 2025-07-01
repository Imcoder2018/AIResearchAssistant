import asyncio
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from src.schemas.chat import ChatRequest
from src.services.openai_service import OpenAIService
import json

router = APIRouter(prefix="/v1", tags=["chat"])

class ChatResponse(BaseModel):
    content: str

@router.post("/")
async def chat(request: ChatRequest):
    openai_service = OpenAIService()
    try:
        content = await openai_service.chat(request.message)
        return {"content": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chat processing error: {str(e)}")
