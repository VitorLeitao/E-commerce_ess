"""versão final do banco

Revision ID: 2c9391c4f3bc
Revises: bbf748d9b646
Create Date: 2023-08-17 15:47:05.163597

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c9391c4f3bc'
down_revision = 'bbf748d9b646'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item', sa.Column('preco_total', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('item', 'preco_total')
    # ### end Alembic commands ###
