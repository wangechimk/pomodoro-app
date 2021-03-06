"""add timer activity  migration

Revision ID: 667ab35bc43f
Revises: a9a7fa31ccbf
Create Date: 2021-04-29 22:31:18.464080

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '667ab35bc43f'
down_revision = 'a9a7fa31ccbf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('activity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('amount_time', sa.Integer(), nullable=True),
    sa.Column('break_time', sa.Integer(), nullable=True),
    sa.Column('break_activity', sa.String(length=300), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('activity')
    # ### end Alembic commands ###
