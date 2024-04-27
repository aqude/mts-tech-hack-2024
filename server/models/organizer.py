import sqlalchemy as sa
from core.database import Base
from sqlalchemy.orm import relationship


class Organizer(Base):
    __tablename__ = "organizers"
    id = sa.Column("id", sa.UUID(as_uuid=True), primary_key=True)
    name = sa.Column("name", sa.String(255), nullable=False)
    description = sa.Column("description", sa.Text, nullable=True)
    events = relationship("GlobalEvent", back_populates="organizer")
