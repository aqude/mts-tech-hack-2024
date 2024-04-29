import uuid
from pydantic import BaseModel


class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str


class LoginRequest(BaseModel):
    phone: str


class RefreshRequest(BaseModel):
    refresh_token: str


class UserResponse(BaseModel):
    id: uuid.UUID
    phone: str
    is_superuser: bool


class UserCreateRequest(BaseModel):
    phone: str
    is_superuser: bool


class UserUpdateRequest(BaseModel):
    id: uuid.UUID
    phone: str
    is_superuser: bool
