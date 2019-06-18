"""Add url to git repository

Revision ID: f40ec634d191
Revises: ebbfb7d55f62
Create Date: 2019-04-02 09:52:17.255944

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f40ec634d191"
down_revision = "ebbfb7d55f62"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("projects", sa.Column("git_url", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("projects", "git_url")
    # ### end Alembic commands ###
