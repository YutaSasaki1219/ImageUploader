from email.mime import image
from urllib import response
import cloudinary
from cloudinary.uploader import upload
import cloudinary.api
import os

DEFAULT_TAG = "image_uploader"
def configure():
    cloudinary.config( 
        cloud_name = os.environ["CLOUD_NAME"],
        api_key = os.environ["API_KEY"],
        api_secret = os.environ["API_SECRET"],
        secure = True
    )

def upload_image(file: bytes):
    print(file)
    try:
        configure()
        response = upload(
            file,
            tags=DEFAULT_TAG
        )
        return response["url"]
    except Exception as e:
        return None
