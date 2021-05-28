"""empty message

Revision ID: a9fba1e59878
Revises: 199cf3a93305
Create Date: 2021-05-22 16:55:47.411841

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9fba1e59878'
down_revision = '199cf3a93305'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('classifier',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('classifier', sa.PickleType(), nullable=True),
    sa.Column('vectorizer', sa.PickleType(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('classifier')
    # ### end Alembic commands ###
