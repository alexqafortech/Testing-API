from pydantic import BaseModel, ConfigDict

class BaseResponse(BaseModel):
    model_config = ConfigDict(extra = "ignore")
    id: str
    created_at: str | None = None
    updated_at: str | None = None