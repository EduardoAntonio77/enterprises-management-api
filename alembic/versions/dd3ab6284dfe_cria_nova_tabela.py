"""cria nova_tabela

Revision ID: dd3ab6284dfe
Revises: 
Create Date: 2025-05-07 18:47:32.183971

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dd3ab6284dfe'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'product_filters',
        sa.Column('filter_id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('filter_name', sa.String(length=100), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('product_id', sa.Integer, sa.ForeignKey('products.id'), nullable=False),
    )
    pass


def downgrade():
    op.drop_table('product_filters')
    pass
