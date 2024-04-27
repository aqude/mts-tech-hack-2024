import sqlalchemy as sa
from core.database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = sa.Column("id", sa.UUID(as_uuid=True), primary_key=True, index=True)
    phone = sa.Column("phone", sa.String(20), unique=True, index=True)
    is_superuser = sa.Column("is_superuser", sa.Boolean, default=False)

    global_events = relationship(
        "GlobalEvent", secondary="global_events_users", back_populates="users"
    )
