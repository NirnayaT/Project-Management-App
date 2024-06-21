from fastapi import FastAPI
from tasks.endpoint import router as tasks_endpoint_router
from Users.endpoint import router as users_endpoint_router

app = FastAPI()

app.include_router(tasks_endpoint_router)
app.include_router(users_endpoint_router)