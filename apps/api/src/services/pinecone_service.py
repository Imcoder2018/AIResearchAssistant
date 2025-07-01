import os
import pinecone
from openai import AsyncOpenAI

async def query_pinecone(query: str, max_results: int = 5) -> list:
    """
    Query Pinecone index for relevant documents based on the input query.
    
    Args:
        query: The search query to find relevant documents.
        max_results: Maximum number of results to return.
    
    Returns:
        A list of document metadata or content snippets matching the query.
    """
    # Initialize OpenAI client for embeddings
    openai_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # Get embedding for the query
    response = await openai_client.embeddings.create(
        input=query,
        model="text-embedding-ada-002"
    )
    query_embedding = response.data[0].embedding
    
    # Initialize Pinecone
    pinecone.init(
        api_key=os.getenv("PINECONE_API_KEY"),
        environment=os.getenv("PINECONE_ENVIRONMENT")
    )
    index_name = "research-assistant"
    
    # Connect to index
    index = pinecone.Index(index_name)
    
    # Query Pinecone for similar vectors
    results = index.query(
        vector=query_embedding,
        top_k=max_results,
        include_metadata=True
    )
    
    # Process results
    formatted_results = []
    for match in results.get('matches', []):
        formatted_results.append({
            "id": match.get('id', ''),
            "score": match.get('score', 0.0),
            "text": match.get('metadata', {}).get('text', ''),
        })
    
    return formatted_results
