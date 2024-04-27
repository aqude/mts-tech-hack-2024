import sqlalchemy as sa
from core.database import Base
from sqlalchemy.orm import relationship


class City(Base):
    __tablename__ = "cities"

    id = sa.Column("id", sa.Integer, primary_key=True)
    name = sa.Column("name", sa.String(255), nullable=False, index=True)
    short_name = sa.Column("short_name", sa.String(255), nullable=False, index=True)
    venues = relationship("Venue", back_populates="city")
