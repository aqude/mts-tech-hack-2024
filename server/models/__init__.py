from .user import User
from core.database import Base

metadata = [model.metadata for model in Base.__subclasses__()]

__all__ = ["User"]
