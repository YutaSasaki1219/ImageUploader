from typing import Optional
from pydantic import BaseModel, Field, HttpUrl

class ImageUploadResponse(BaseModel):
    url: Optional[HttpUrl] = Field(None)