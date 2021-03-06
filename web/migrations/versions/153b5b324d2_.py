"""empty message

Revision ID: 153b5b324d2
Revises: 2d09945ea13
Create Date: 2021-02-23 15:00:09.237922

"""

# revision identifiers, used by Alembic.
revision = '153b5b324d2'
down_revision = '2d09945ea13'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('detection_times',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('host', sa.String(length=256), nullable=False),
    sa.Column('date', sa.Time(), nullable=True),
    sa.Column('hour', sa.Integer(), nullable=True),
    sa.Column('reason', sa.String(length=256), nullable=True),
    sa.Column('ban_expired_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('requests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ip_address', sa.String(length=256), nullable=False),
    sa.Column('path', sa.String(length=256), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('user_agent', sa.String(length=256), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('method', sa.String(length=4), nullable=True),
    sa.Column('size', sa.Integer(), nullable=True),
    sa.Column('referrer', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('requests')
    op.drop_table('detection_times')
    ### end Alembic commands ###
