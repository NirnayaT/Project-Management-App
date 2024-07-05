from fastapi import FastAPI
from tasks.endpoint import router as tasks_endpoint_router
from Users.endpoint import router as users_endpoint_router
from Project.endpoint import router as projects_endpoint_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tasks_endpoint_router)
app.include_router(users_endpoint_router)
app.include_router(projects_endpoint_router)
