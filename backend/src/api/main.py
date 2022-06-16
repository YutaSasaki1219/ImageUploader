from fastapi import FastAPI
from api.routers import image

app = FastAPI()
app.include_router(image.router)
