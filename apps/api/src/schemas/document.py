from pydantic import BaseModel

class DocumentStatus(BaseModel):
    message: str
    filename: str
