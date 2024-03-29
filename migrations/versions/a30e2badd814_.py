"""empty message

Revision ID: a30e2badd814
Revises: 36eaa4dcc719
Create Date: 2019-11-21 16:47:39.741671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a30e2badd814'
down_revision = '36eaa4dcc719'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('Customer',
    sa.Column('customer_ID', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('balance', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_ID'], ['Users.user_id'], ),
    sa.PrimaryKeyConstraint('customer_ID')
    )
    op.drop_table('customer')
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.INTEGER(), server_default=sa.text("nextval('users_user_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('user_id', name='users_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('customer',
    sa.Column('customer_ID', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('balance', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['customer_ID'], ['users.user_id'], name='customer_customer_ID_fkey'),
    sa.PrimaryKeyConstraint('customer_ID', name='customer_pkey')
    )
    op.drop_table('Customer')
    op.drop_table('Users')
    # ### end Alembic commands ###
