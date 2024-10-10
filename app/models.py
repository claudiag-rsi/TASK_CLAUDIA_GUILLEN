from pydantic import BaseModel
from typing import Optional, List


class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    completed: bool = False


class UpdateTaskModel(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class TaskList(BaseModel):
    tasks: List[Task]
