import sqlalchemy as sa
from core.database import Base
from sqlalchemy.orm import relationship


class Tag(Base):
    __tablename__ = "tags"

    name = sa.Column("name", sa.String(255), primary_key=True)
    events = relationship(
        "GlobalEvent", secondary="global_events_tags", back_populates="tags"
    )
