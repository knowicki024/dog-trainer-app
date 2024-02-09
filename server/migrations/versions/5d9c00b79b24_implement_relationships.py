"""implement relationships

Revision ID: 5d9c00b79b24
Revises: 3d4e9644fda2
Create Date: 2024-02-07 10:26:33.788560

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d9c00b79b24'
down_revision = '3d4e9644fda2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('signups', sa.Column('activity_id', sa.Integer(), nullable=True))
    op.add_column('signups', sa.Column('camper_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_signups_camper_id_campers'), 'signups', 'campers', ['camper_id'], ['id'])
    op.create_foreign_key(op.f('fk_signups_activity_id_activities'), 'signups', 'activities', ['activity_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_signups_activity_id_activities'), 'signups', type_='foreignkey')
    op.drop_constraint(op.f('fk_signups_camper_id_campers'), 'signups', type_='foreignkey')
    op.drop_column('signups', 'camper_id')
    op.drop_column('signups', 'activity_id')
    # ### end Alembic commands ###
