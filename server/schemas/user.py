from pydantic import BaseModel


class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str


class LoginRequest(BaseModel):
    phone: str


class RefreshRequest(BaseModel):
    refresh_token: str


class UserResponse(BaseModel):
    phone: str
