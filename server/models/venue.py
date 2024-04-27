import sqlalchemy as sa
from core.database import Base
from sqlalchemy.orm import Mapped, relationship
from .city import City


class Venue(Base):
    __tablename__ = "venues"

    id = sa.Column("id", sa.UUID(as_uuid=True), primary_key=True)
    title = sa.Column("title", sa.String(255), nullable=False, index=True)
    address = sa.Column("address", sa.String(255), nullable=False)
    city_id = sa.Column(
        "city_id",
        sa.Integer,
        sa.ForeignKey("cities.id", ondelete="CASCADE"),
        nullable=False,
    )
    city: Mapped["City"] = relationship("City", back_populates="venues")
    events = relationship("GlobalEvent", back_populates="venue")
