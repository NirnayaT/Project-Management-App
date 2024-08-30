"""Add is_verified and is_active column to User table

Revision ID: c3f43f62640c
Revises: 7b5528a3f83f
Create Date: 2024-08-28 09:20:49.553488

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c3f43f62640c'
down_revision: Union[str, None] = '7b5528a3f83f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('is_active', sa.Boolean(), nullable=True))
    op.add_column('users', sa.Column('is_admin', sa.Boolean(), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'is_admin')
    op.drop_column('users', 'is_active')
