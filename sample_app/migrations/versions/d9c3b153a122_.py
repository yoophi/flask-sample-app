"""empty message

Revision ID: d9c3b153a122
Revises: 0218dc5cde5c
Create Date: 2016-05-30 19:00:32.289031

"""

# revision identifiers, used by Alembic.
revision = 'd9c3b153a122'
down_revision = '0218dc5cde5c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('title', sa.Unicode(), nullable=True),
    sa.Column('text', sa.UnicodeText(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    ### end Alembic commands ###