import pytest
import json
from fastapi.testclient import TestClient
from httpx import AsyncClient
from unittest.mock import patch, AsyncMock
from src.main import app

@pytest.mark.asyncio
async def test_chat_integration_with_tool_call():
    """
    Test the full chat flow with a tool call to search scientific papers.
    Mocks the Pinecone query response and verifies the assistant's final response.
    """
    # Mock the Pinecone query function
    mock_pinecone_results = [
        {
            "id": "doc1",
            "score": 0.85,
            "text": "This is a relevant scientific paper about AI advancements."
        },
        {
            "id": "doc2",
            "score": 0.78,
            "text": "Another paper discussing AI in research contexts."
        }
    ]
    
    with patch('src.services.pinecone_service.query_pinecone', new=AsyncMock(return_value=mock_pinecone_results)):
        async with AsyncClient(app=app, base_url="http://test") as ac:
            # Send a chat message that should trigger a tool call
            response = await ac.post(
                "/v1/chat",
                json={
                    "message": "Can you find recent papers about AI in research?",
                    "thread_id": None
                },
                headers={"Content-Type": "application/json"}
            )
            
            assert response.status_code == 200
            
            # Process the streaming response
            content = ""
            async for chunk in response.content.iter_any():
                try:
                    data = json.loads(chunk.decode('utf-8'))
                    if "content" in data and data["content"]:
                        content += data["content"]
                except json.JSONDecodeError:
                    continue
            
            # Assert that the response contains information from the mocked tool output
            assert "AI advancements" in content or "AI in research" in content, \
                f"Expected tool call results in response, but got: {content}"
