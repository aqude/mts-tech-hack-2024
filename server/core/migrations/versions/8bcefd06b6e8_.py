"""empty message

Revision ID: 8bcefd06b6e8
Revises: 2d1644c1b28a
Create Date: 2024-04-27 17:44:02.406949

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "8bcefd06b6e8"
down_revision: Union[str, None] = "2d1644c1b28a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "cities",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_cities_name"), "cities", ["name"], unique=False)
    op.create_table(
        "organizers",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "tags",
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("name"),
    )
    op.create_table(
        "venues",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("address", sa.String(length=255), nullable=False),
        sa.Column("city_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["city_id"], ["cities.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_venues_title"), "venues", ["title"], unique=False)
    op.create_table(
        "global_events",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("date", sa.DateTime(), nullable=False),
        sa.Column("organizer_id", sa.UUID(), nullable=False),
        sa.Column("venue_id", sa.UUID(), nullable=False),
        sa.Column("tickets", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["organizer_id"], ["organizers.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(["venue_id"], ["venues.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_global_events_title"), "global_events", ["title"], unique=False
    )
    op.create_table(
        "global_events_tags",
        sa.Column("global_event_id", sa.UUID(), nullable=False),
        sa.Column("tag_id", sa.String(length=255), nullable=False),
        sa.ForeignKeyConstraint(
            ["global_event_id"], ["global_events.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(["tag_id"], ["tags.name"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("global_event_id", "tag_id"),
    )
    op.create_table(
        "global_events_users",
        sa.Column("global_event_id", sa.UUID(), nullable=False),
        sa.Column("user_id", sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["global_event_id"], ["global_events.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("global_event_id", "user_id"),
    )
    op.add_column("users", sa.Column("is_superuser", sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "is_superuser")
    op.drop_table("global_events_users")
    op.drop_table("global_events_tags")
    op.drop_index(op.f("ix_global_events_title"), table_name="global_events")
    op.drop_table("global_events")
    op.drop_index(op.f("ix_venues_title"), table_name="venues")
    op.drop_table("venues")
    op.drop_table("tags")
    op.drop_table("organizers")
    op.drop_index(op.f("ix_cities_name"), table_name="cities")
    op.drop_table("cities")
    # ### end Alembic commands ###
