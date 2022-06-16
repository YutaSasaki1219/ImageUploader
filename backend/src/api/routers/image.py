from fastapi import APIRouter, File, UploadFile, HTTPException
from api.schema import image as image_schema
import os, shutil
from api.external_service import image_uploader

router = APIRouter()

@router.post("/images", response_model=image_schema.ImageUploadResponse)
async def upload_image(upload_file: UploadFile = File(...)):
      url = image_uploader.upload_image(upload_file.file)
      print(url)
      if url == None:
         raise HTTPException(status_code=500, detail="internal_server_error") 
      return image_schema.ImageUploadResponse(url=url)
