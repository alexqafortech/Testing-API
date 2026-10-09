from pydantic import BaseModel, ConfigDict, model_validator
from models.base import BaseResponse
from typing import Literal

class TaskResponse(BaseResponse):
    title: str
    description: str | None = None
    status: Literal["TODO", "IN_PROGRESS", "COMPLETED", "ARCHIVED"]
    priority: Literal["LOW", "MEDIUM", "HIGH", "URGENT"]
    due_date: str | None = None
    category_id: str | None = None
    user_id: str
    is_overdue: bool
    @model_validator(mode="after")
    def check_dates(self):
        if self.created_at and self.updated_at:
            if self.updated_at < self.created_at:
                raise ValueError("updated_at не может быть раньше created_at")
        return self

class TaskListResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")
    items: list[TaskResponse]
    total: int
    page: int
    page_size: int
    total_pages: int