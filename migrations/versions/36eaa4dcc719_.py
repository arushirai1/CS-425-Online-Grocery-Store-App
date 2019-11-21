"""empty message

Revision ID: 36eaa4dcc719
Revises: d28daa0819ba
Create Date: 2019-11-21 16:46:32.480225

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36eaa4dcc719'
down_revision = 'd28daa0819ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer',
    sa.Column('customer_ID', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('balance', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_ID'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('customer_ID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('customer')
    # ### end Alembic commands ###