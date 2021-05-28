"""empty message

Revision ID: 5ed5d3f8bae8
Revises: a549475786d7
Create Date: 2021-05-20 20:47:28.371618

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ed5d3f8bae8'
down_revision = 'a549475786d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('news',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('news_title', sa.Text(), nullable=True),
    sa.Column('news_summarized', sa.Text(), nullable=True),
    sa.Column('searched_keyword', sa.Text(), nullable=True),
    sa.Column('url_link', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('news')
    # ### end Alembic commands ###