"""
Provides an API router for managing tasks.

The `tasks_router` handles the following endpoints:

- `POST /`: Creates a new task.
- `GET /{task_id}`: Retrieves a specific task by its ID.
- `GET /`: Retrieves a list of all tasks.
- `PUT /{task_id}`: Updates an existing task by its ID.
- `DELETE /`: Deletes all tasks.
- `DELETE /{task_id}`: Deletes a specific task by its ID.
"""
import logging
from fastapi import APIRouter, HTTPException
from models import Task, UpdateTaskModel, TaskList
from db import db

# Configuración del logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

tasks_router = APIRouter()


@tasks_router.post("/", response_model=Task)
async def create_task(task: Task):
     logger.info(f"Creando nueva tarea: {task.title}")
     return db.add_task(task)


@tasks_router.get("/{task_id}", response_model=Task)
async def get_task(task_id: int):
    logger.info(f"Obteniendo tarea con ID: {task_id}")
    task = db.get_task(task_id)
    if task is None:
        logger.warning(f"Tarea con ID {task_id} no encontrada")
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@tasks_router.get("/", response_model=TaskList)
async def get_tasks():
    tasks = db.get_tasks()
    return TaskList(tasks=tasks)


@tasks_router.put("/{task_id}", response_model=Task)
async def update_task(task_id: int, task_update: UpdateTaskModel):
    logger.info(f"Actualizando tarea con ID: {task_id}")
    updated_task = db.update_task(task_id, task_update)
    if updated_task is None:
        logger.warning(f"Tarea con ID {task_id} no encontrada para actualizar")
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@tasks_router.delete("/all")
async def delete_all_tasks():
    # logger.info("Eliminando todas las tareas")
    db.delete_all_tasks()
    return {"mensaje": "Todas las tareas han sido eliminadas"}

@tasks_router.delete("/{task_id}")
async def delete_task(task_id: int):
    logger.info(f"Eliminando tarea con ID: {task_id}")
    db.delete_task(task_id)
    return {"message": "Task deleted successfully"}

