from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from utils.sockets.handler import router as sockets_router
from routers.api import router as api_router
from htmlexample import html

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def main():
    return HTMLResponse(html)  # {"Welcome": "to Project Management App."}


app.include_router(sockets_router)
app.include_router(api_router)
