from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from utils.sockets.handler import router as sockets_router
from routers.api import router as api_router
from htmlexample import html
from fastapi.staticfiles import StaticFiles

file_path = "C:/Users/nirna/OneDrive/Desktop/ProjectManagamentApp/server/images"

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
    """
    Renders the HTML response for the root path ("/") of the FastAPI 
    application.
    
    Returns:
        HTMLResponse: The HTML response to be returned to the client.
    """
        
    return HTMLResponse(html)  # {"Welcome": "to Project Management App."}


app.include_router(sockets_router)
app.include_router(api_router)
app.mount("/static/images", StaticFiles(directory=f"{file_path}"), name="static")
