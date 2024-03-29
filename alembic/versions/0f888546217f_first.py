"""first

Revision ID: 0f888546217f
Revises: 
Create Date: 2019-10-14 15:33:59.160912+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f888546217f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('visited', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('post',
    sa.Column('message_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(length=1024), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('message_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    op.drop_table('user')
    # ### end Alembic commands ###
