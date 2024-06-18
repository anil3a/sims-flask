"""Add Activitylog model.

Revision ID: 366fbb91c1d4
Revises: dadf2eee2b9b
Create Date: 2024-06-18 06:20:20.770090

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '366fbb91c1d4'
down_revision = 'dadf2eee2b9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('activitylog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('action', sa.String(length=128), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('rel_text', sa.String(length=64), nullable=True),
    sa.Column('rel_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('activitylog')
    # ### end Alembic commands ###