"""empty message

Revision ID: 49be439fccb8
Revises: a28927b53269
Create Date: 2019-11-21 16:02:53.185213

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49be439fccb8'
down_revision = 'a28927b53269'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
