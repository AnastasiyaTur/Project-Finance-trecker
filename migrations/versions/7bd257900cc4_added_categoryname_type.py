"""Added CategoryName.type

Revision ID: 7bd257900cc4
Revises: db9868cfd74c
Create Date: 2022-10-21 17:32:53.873044

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7bd257900cc4'
down_revision = 'db9868cfd74c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category_name', sa.Column('type', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('category_name', 'type')
    # ### end Alembic commands ###
