from models.base import BaseResponse
from pydantic import BaseModel

class CategoryResponse(BaseResponse):
    name: str
    color: str | None = None
    user_id: str

class CategoryStatsResponse(BaseModel):
    category: CategoryResponse
    task_count: int | None = None
