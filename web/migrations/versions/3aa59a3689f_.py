"""empty message

Revision ID: 3aa59a3689f
Revises: 5937ad6a262
Create Date: 2021-01-24 10:42:32.515920

"""

# revision identifiers, used by Alembic.
revision = '3aa59a3689f'
down_revision = '5937ad6a262'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('requests', sa.Column('path', sa.String(length=256), nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('requests', 'path')
    ### end Alembic commands ###
