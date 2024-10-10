from fastapi import FastAPI
from routers.tasks_router import tasks_router

app = FastAPI()

app.include_router(tasks_router, prefix="/tasks", tags=["tasks"])


@app.get("/")
async def root():
    return {"message": "Task Manager API"}
