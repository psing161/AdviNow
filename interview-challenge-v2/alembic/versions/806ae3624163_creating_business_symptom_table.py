"""Creating business_symptom table

Revision ID: 806ae3624163
Revises: 
Create Date: 2024-11-22 15:32:23.364895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '806ae3624163'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('business_symptom',
    sa.Column('business_id', sa.Integer(), nullable=False),
    sa.Column('business_name', sa.String(length=100), nullable=False),
    sa.Column('symptom_code', sa.String(length=100), nullable=False),
    sa.Column('symptom_name', sa.String(length=100), nullable=False),
    sa.Column('symptom_diagnostic', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('business_id', 'symptom_code', name='pk_business_symptom')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('business_symptom')
    # ### end Alembic commands ###
