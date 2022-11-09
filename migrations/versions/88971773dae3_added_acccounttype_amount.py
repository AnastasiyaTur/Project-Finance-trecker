"""Added AcccountType.amount

Revision ID: 88971773dae3
Revises: 20e005582a88
Create Date: 2022-10-24 12:49:12.689610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88971773dae3'
down_revision = '20e005582a88'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('account_type', sa.Column('amount', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('account_type', 'amount')
    # ### end Alembic commands ###
