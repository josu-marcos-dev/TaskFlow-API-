from pydantic import BaseModel
from datetime import datetime
from typing import Literal, Optional

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    priority: Optional[int] = None

class CreateTask(TaskBase):
    status: Literal["pending", "in_progress", "completed"]
    project_id: int

class UpdateTask(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[int] = None
    status: Optional[str] = None
class ResponseTask(TaskBase):
    task_id: int
    project_id: int
    creation_date: datetime 
    model_config = {"from_attributes": True}