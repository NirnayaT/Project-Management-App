"""deleted fullname in the table.

Revision ID: 0522e1f0374a
Revises: 28168e2c868a
Create Date: 2024-07-24 10:49:25.123138

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0522e1f0374a'
down_revision: Union[str, None] = '28168e2c868a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
