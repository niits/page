"""empty message

Revision ID: 2319d5a8cfd
Revises: 2acf62365a2
Create Date: 2021-02-27 08:28:15.053784

"""

# revision identifiers, used by Alembic.
revision = '2319d5a8cfd'
down_revision = '2acf62365a2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('requests', sa.Column('hash_id', sa.String(length=256), nullable=False))
    op.drop_column('requests', 'is_main_request')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('requests', sa.Column('is_main_request', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('requests', 'hash_id')
    ### end Alembic commands ###
