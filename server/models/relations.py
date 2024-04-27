import sqlalchemy as sa
from core.database import Base


class GlobalEventsTags(Base):
    __tablename__ = "global_events_tags"

    global_event_id = sa.Column(
        "global_event_id",
        sa.UUID(as_uuid=True),
        sa.ForeignKey("global_events.id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    )
    tag_id = sa.Column(
        "tag_id",
        sa.String(255),
        sa.ForeignKey("tags.name", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    )


class GlobalEventsUsers(Base):
    __tablename__ = "global_events_users"

    global_event_id = sa.Column(
        "global_event_id",
        sa.UUID(as_uuid=True),
        sa.ForeignKey("global_events.id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    )
    user_id = sa.Column(
        "user_id",
        sa.UUID(as_uuid=True),
        sa.ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    )
