import asyncio
from typing import List
import os
from fastapi import UploadFile
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from openai import AsyncOpenAI
import pinecone
import uuid

async def process_pdf_and_upsert(file: UploadFile) -> dict:
    """
    Process a PDF file, extract text, create embeddings, and upsert to Pinecone.
    
    Args:
        file: The uploaded PDF file.
    
    Returns:
        A dictionary with status message and filename.
    """
    # Read PDF content
    content = await file.read()
    
    # Extract text using pypdf (synchronous operation wrapped in asyncio.to_thread)
    def extract_text(pdf_content: bytes) -> str:
        reader = PdfReader(io.BytesIO(pdf_content))
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    
    text = await asyncio.to_thread(extract_text, content)
    
    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    
    # Get embeddings for chunks using OpenAI API
    openai_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    embeddings = []
    for chunk in chunks:
        response = await openai_client.embeddings.create(
            input=chunk,
            model="text-embedding-ada-002"
        )
        embeddings.append(response.data[0].embedding)
    
    # Initialize Pinecone
    pinecone.init(
        api_key=os.getenv("PINECONE_API_KEY"),
        environment=os.getenv("PINECONE_ENVIRONMENT")
    )
    index_name = "research-assistant"
    
    # Create or connect to index
    if index_name not in pinecone.list_indexes():
        pinecone.create_index(
            name=index_name,
            dimension=1536,  # Dimension for text-embedding-ada-002
            metric="cosine"
        )
    index = pinecone.Index(index_name)
    
    # Upsert vectors to Pinecone
    vectors = [(str(uuid.uuid4()), embedding, {"text": chunk}) 
               for embedding, chunk in zip(embeddings, chunks)]
    index.upsert(vectors)
    
    return {"message": "Document processed and vectors upserted successfully", "filename": file.filename}
