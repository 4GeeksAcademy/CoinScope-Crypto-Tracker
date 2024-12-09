"""empty message

<<<<<<<< HEAD:migrations/versions/862c2c0a794e_.py
Revision ID: 862c2c0a794e
Revises: 
Create Date: 2024-12-05 18:12:13.488976
========
Revision ID: 29c7fe7642a3
Revises: 
Create Date: 2024-12-05 19:17:10.414072
>>>>>>>> d1dab542c92303f5cab5f08ea829ca8a1266468d:migrations/versions/29c7fe7642a3_.py

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
<<<<<<<< HEAD:migrations/versions/862c2c0a794e_.py
revision = '862c2c0a794e'
========
revision = '29c7fe7642a3'
>>>>>>>> d1dab542c92303f5cab5f08ea829ca8a1266468d:migrations/versions/29c7fe7642a3_.py
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('username', sa.String(length=200), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('coin_id', sa.String(length=30), nullable=True),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('symbol', sa.String(length=20), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('wallet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('coin_id', sa.String(length=10), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('symbol', sa.String(length=20), nullable=True),
    sa.Column('purchase_price', sa.String(length=20), nullable=True),
    sa.Column('purchase_quantity', sa.String(length=20), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wallet')
    op.drop_table('favorites')
    op.drop_table('user')
    # ### end Alembic commands ###
