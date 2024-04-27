import sqlalchemy as sa
from sqlalchemy.orm import Mapped, relationship
from core.database import Base
from models.organizer import Organizer
from models.venue import Venue


class GlobalEvent(Base):
    __tablename__ = "global_events"

    id = sa.Column("id", sa.UUID(as_uuid=True), primary_key=True)
    title = sa.Column("title", sa.String(255), nullable=False, index=True)
    description = sa.Column("description", sa.Text, nullable=True)
    date = sa.Column("date", sa.DateTime, nullable=False)
    organizer_id = sa.Column(
        "organizer_id",
        sa.UUID(as_uuid=True),
        sa.ForeignKey("organizers.id", ondelete="CASCADE"),
        nullable=False,
    )
    organizer: Mapped["Organizer"] = relationship("Organizer", back_populates="events")
    venue_id = sa.Column(
        "venue_id",
        sa.UUID(as_uuid=True),
        sa.ForeignKey("venues.id", ondelete="CASCADE"),
        nullable=False,
    )
    venue: Mapped["Venue"] = relationship("Venue", back_populates="events")
    tickets = sa.Column("tickets", sa.Integer, nullable=False, default=0)
    tags = relationship("Tag", secondary="global_events_tags", back_populates="events")
    users = relationship(
        "User", secondary="global_events_users", back_populates="global_events"
    )
