"""Changes schema

Revision ID: 17cf817f6352
Revises: cce8ac53e631
Create Date: 2018-09-13 13:06:23.005851

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17cf817f6352'
down_revision = 'cce8ac53e631'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_pitch_category', table_name='pitch')
    op.create_index(op.f('ix_pitch_category'), 'pitch', ['category'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_pitch_category'), table_name='pitch')
    op.create_index('ix_pitch_category', 'pitch', ['category'], unique=True)
    # ### end Alembic commands ###
