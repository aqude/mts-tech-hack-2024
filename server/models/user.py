import sqlalchemy as sa
from core.database import Base


class User(Base):
    __tablename__ = "users"

    id = sa.Column("id", sa.UUID(as_uuid=True), primary_key=True, index=True)
    phone = sa.Column("phone", sa.String(20), unique=True, index=True)
