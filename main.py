from fastapi import FastAPI
from tasks.endpoint import router as endpoint_router

app = FastAPI()

app.include_router(endpoint_router)