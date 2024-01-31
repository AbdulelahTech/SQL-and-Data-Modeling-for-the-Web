"""empty message

Revision ID: d28c3ae1cdfe
Revises: 8a6129bb8ac3
Create Date: 2024-01-31 11:25:13.753545

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd28c3ae1cdfe'
down_revision = '8a6129bb8ac3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Artist', 'image_link',
               existing_type=sa.VARCHAR(length=1000),
               type_=sa.String(length=5000),
               existing_nullable=True)
    op.alter_column('Venue', 'image_link',
               existing_type=sa.VARCHAR(length=1000),
               type_=sa.String(length=5000),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Venue', 'image_link',
               existing_type=sa.String(length=5000),
               type_=sa.VARCHAR(length=1000),
               existing_nullable=True)
    op.alter_column('Artist', 'image_link',
               existing_type=sa.String(length=5000),
               type_=sa.VARCHAR(length=1000),
               existing_nullable=True)
    # ### end Alembic commands ###
