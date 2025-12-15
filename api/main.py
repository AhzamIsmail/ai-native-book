from fastapi import FastAPI, HTTPException
from typing import List, Optional, Dict, Any
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
import sys
import os
# Add backend to path to import services and models
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from backend.services.rag_service import rag_service
from backend.models.entities import Source
import logging
from backend.logger import logger


class ChatRequest(BaseModel):
    query: str
    top_k: Optional[int] = 5


class ChatResponse(BaseModel):
    answer: str
    sources: List[Dict[str, Any]]


class SelectedTextChatRequest(BaseModel):
    query: str
    context: str  # Can be raw text or chunk IDs (for now we'll handle raw text)
    top_k: Optional[int] = 5


app = FastAPI(title="RAG Chatbot API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    logger.info("Root endpoint accessed")
    return {"message": "RAG Chatbot API"}


@app.post("/api/v1/chat", response_model=ChatResponse)
async def chat_full_book(request: ChatRequest):
    """
    Full-book RAG chat endpoint
    Allows users to ask questions about the full book content and receive answers based on the entire book
    """
    logger.info(f"Full book query received: {request.query[:50]}...")

    try:
        # Use the RAG service to query the full book
        response = rag_service.query_full_book(request.query, request.top_k)

        # Format sources for the response
        formatted_sources = [
            {
                "page": source.page_number,
                "text": source.text
            }
            for source in response.sources
        ]

        logger.info(f"Full book query processed successfully, sources: {len(formatted_sources)}")

        return ChatResponse(
            answer=response.response_text,
            sources=formatted_sources
        )
    except Exception as e:
        logger.error(f"Error processing full book query: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")


@app.post("/api/v1/chat-selected", response_model=ChatResponse)
async def chat_selected_text(request: SelectedTextChatRequest):
    """
    Isolated RAG chat for selected text
    Allows users to ask questions about user-selected text without contamination from full-book content
    """
    logger.info(f"Selected text query received: {request.query[:50]}...")

    try:
        # Use the RAG service to query the selected text only
        response = rag_service.query_selected_text(request.query, request.context)

        # Format sources for the response
        formatted_sources = [
            {
                "page": source.page_number,
                "text": source.text
            }
            for source in response.sources
        ]

        logger.info(f"Selected text query processed successfully, sources: {len(formatted_sources)}")

        return ChatResponse(
            answer=response.response_text,
            sources=formatted_sources
        )
    except Exception as e:
        logger.error(f"Error processing selected text query: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")


# Add exception handlers for common errors
@app.exception_handler(404)
async def custom_http_exception_handler(request, exc):
    logger.warning(f"404 error: {request.url}")
    return {"message": "Endpoint not found"}


@app.exception_handler(500)
async def validation_exception_handler(request, exc):
    logger.error(f"500 server error: {str(exc)}", exc_info=True)
    return {"message": "Internal server error"}


# Mangum handler for Vercel serverless deployment
handler = Mangum(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)