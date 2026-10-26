from models.base import BaseResponse
from pydantic import BaseModel

class UserResponse(BaseResponse):
    email: str
    username: str
    is_active: bool | None = None
    is_verified: bool | None = None
    full_name: str | None = None
    is_admin: bool | None = None