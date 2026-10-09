from pydantic import BaseModel, Field

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str | None
    token_type: str

class RegisterPayload(BaseModel):
    email: str = Field(min_length=5)
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=8)