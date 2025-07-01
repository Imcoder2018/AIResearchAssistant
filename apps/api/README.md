# AI Research Assistant: Backend (FastAPI)

Made completely with Windsurf AI

---

## 📚 Project Overview

This is the backend component of the AI Research Assistant application, built with FastAPI to deliver a robust and asynchronous API for managing AI-powered research workflows. It resides in a monorepo alongside the Next.js frontend, enabling consistent development and deployment practices.

---

## ✨ Features

- Modular Project Structure  
  - Organized into `src/api/v1`, `src/core`, `src/schemas`, and `src/services` for clarity and scalability.

- Pydantic Schemas  
  - Handles data validation and serialization with `ChatRequest` (for chat messages) and `DocumentStatus` (for processing feedback).

- OpenAI Service Integration  
  - Manages interactions with the OpenAI API for chat threads, messages, runs, and streaming completions.  
  - Migrated from Assistants v1 to the stable Chat Completions API to avoid deprecation.

- Document Processing Service  
  - Uploads and reads PDFs asynchronously using `pypdf` wrapped in `asyncio.to_thread`.  
  - Splits extracted text into chunks, generates OpenAI embeddings, and upserts into a Pinecone index.

- API Routers  
  - **POST /upload**: Ingests documents via `process_pdf_and_upsert`.  
  - **POST /**: Orchestrates chat loops, thread management, message handling, and streams AI responses.

- AI Agent Tooling  
  - Defines function-calling tools like `search_scientific_papers` (Pinecone query) and `search_arxiv` (ArXiv Python library).

- Containerization  
  - Fully Dockerized for consistent, portable deployments.

---

## 🛠️ Technologies Used

- Python 3.11  
- FastAPI  
- uvicorn (ASGI server)  
- Pydantic (data validation)  
- OpenAI Python SDK  
- Pinecone Client  
- pypdf  
- langchain (text splitting)  
- arxiv (Python library)  
- httpx (HTTP client)  
- pytest & pytest-asyncio (integration testing)  
- Docker  
- pnpm (monorepo management)

---

## ⚙️ Setup and Installation (Local Development)

1. Clone the monorepo  
   ```bash
   git clone <your-repo-url>
   ```

2. Navigate to the backend directory  
   ```bash
   cd apps/api
   ```

3. Create and populate the `.env` file (or copy from `.env.example`) with your API keys.

4. Docker Setup  
   - Install Docker Desktop for your OS.  
   - Build the Docker image:  
     ```bash
     docker build -t ai-research-backend .
     ```  
   - Run the container:  
     ```bash
     docker run -d \
       --name ai-backend \
       -p 8001:8000 \
       --env-file .env \
       -v $(pwd)/src:/app/src \
       ai-research-backend
     ```

5. Verify the backend  
   - Open Swagger UI at `http://localhost:8001/docs`.  
   - Confirm `/v1/` (chat) and `/v1/upload` (documents) endpoints appear.  
   - Test the chat endpoint to ensure a response like `{"content":"Hello! How can I assist you today?"}`.

---

## 🧪 Integration Testing

The backend includes integration tests using pytest and pytest-asyncio.

1. Install testing dependencies (outside Docker):  
   ```bash
   pip install pytest pytest-asyncio httpx
   ```

2. Run the tests:  
   ```bash
   pytest
   ```

3. These tests mock external services (Pinecone, ArXiv) to simulate full chat and document workflows, validating API logic end to end.

---

## 🚀 Deployment

This backend is optimized for Docker-based deployment.  

Backend URL (Vercel): https://ainextfastapibackend-f73o9zd42-imcoder2018s-projects.vercel.app/docs
