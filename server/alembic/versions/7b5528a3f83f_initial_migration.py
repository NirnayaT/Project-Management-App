"""Initial migration

Revision ID: 7b5528a3f83f
Revises: 
Create Date: 2024-08-22 13:47:25.998984

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7b5528a3f83f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('email', name='unique_user_constraint')
    )
    op.create_table('images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.String(), nullable=False),
    sa.Column('path', sa.String(), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('upload_date', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_images_filename'), 'images', ['filename'], unique=True)
    op.create_index(op.f('ix_images_id'), 'images', ['id'], unique=False)
    op.create_table('projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=False),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task', sa.String(length=100), nullable=False),
    sa.Column('status', sa.Enum('TODO', 'INPROGRESS', 'FINISHED', name='taskstatus'), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.Column('due_date', sa.Date(), nullable=True),
    sa.Column('priority', sa.Enum('LOW', 'MEDIUM', 'HIGH', name='taskpriority'), nullable=False),
    sa.Column('assignee_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['assignee_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('tasks')
    op.drop_table('projects')
    op.drop_index(op.f('ix_images_id'), table_name='images')
    op.drop_index(op.f('ix_images_filename'), table_name='images')
    op.drop_table('images')
    op.drop_table('users')
