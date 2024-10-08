"""Add is_verified column to User table

Revision ID: 87d6db13933f
Revises: c3f43f62640c
Create Date: 2024-08-28 10:04:37.071032

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '87d6db13933f'
down_revision: Union[str, None] = 'c3f43f62640c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('is_verified', sa.Boolean(), nullable=True))
    op.drop_column('users', 'is_admin')


def downgrade() -> None:
    op.add_column('users', sa.Column('is_admin', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('users', 'is_verified')
