"""Add vip to stats

Revision ID: 102580ac9fea
Revises: 0121ad1ee475
Create Date: 2022-01-23 14:42:26.960991

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '102580ac9fea'
down_revision = '0121ad1ee475'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('player_at_count', sa.Column('vip', sa.Boolean(), nullable=True))
    op.add_column('server_counts', sa.Column('vip_count', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('server_counts', 'vip_count')
    op.drop_column('player_at_count', 'vip')
    # ### end Alembic commands ###