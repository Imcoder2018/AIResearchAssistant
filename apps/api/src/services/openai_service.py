from typing import Any
import os
import logging
from openai import AsyncOpenAI

class OpenAIService:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")
        logging.info(f"Initializing AsyncOpenAI client with api_key: {api_key[:4]}****")
        self.client = AsyncOpenAI(api_key=api_key)
        logging.info("AsyncOpenAI client initialized")
    
    async def chat(self, message: str) -> str:
        try:
            response = await self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": message}]
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"Chat processing error: {str(e)}")