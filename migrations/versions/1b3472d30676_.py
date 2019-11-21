"""empty message

Revision ID: 1b3472d30676
Revises: 94a0e20935c5
Create Date: 2019-11-21 17:10:55.069668

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b3472d30676'
down_revision = '94a0e20935c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('credit_card',
    sa.Column('customer_ID', sa.Integer(), nullable=False),
    sa.Column('card_number', sa.Integer(), nullable=False),
    sa.Column('street_address', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('zip_code', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_ID'], ['customer.customer_ID'], ),
    sa.PrimaryKeyConstraint('customer_ID', 'card_number')
    )
    op.create_table('customer_address',
    sa.Column('customer_ID', sa.Integer(), nullable=False),
    sa.Column('street_address', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('zip_code', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_ID'], ['customer.customer_ID'], ),
    sa.PrimaryKeyConstraint('customer_ID')
    )
    op.create_table('pricing',
    sa.Column('product_ID', sa.Integer(), nullable=False),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('price', sa.Numeric(), nullable=True),
    sa.ForeignKeyConstraint(['product_ID'], ['customer.customer_ID'], ),
    sa.PrimaryKeyConstraint('product_ID')
    )
    op.add_column('test', sa.Column('name', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('test', 'name')
    op.drop_table('pricing')
    op.drop_table('customer_address')
    op.drop_table('credit_card')
    # ### end Alembic commands ###
