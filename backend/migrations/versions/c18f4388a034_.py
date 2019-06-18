"""empty message

Revision ID: c18f4388a034
Revises: f40ec634d191
Create Date: 2019-06-03 13:50:25.250824

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c18f4388a034"
down_revision = "f40ec634d191"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "tags",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=40), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "tags_models",
        sa.Column("tag_id", sa.Integer(), nullable=True),
        sa.Column("model_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["model_id"], ["models.id"]),
        sa.ForeignKeyConstraint(["tag_id"], ["tags.id"]),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("tags_models")
    op.drop_table("tags")
    # ### end Alembic commands ###
