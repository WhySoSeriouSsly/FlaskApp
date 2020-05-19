"""empty message

Revision ID: b7bcc18fc765
Revises: 
Create Date: 2020-02-13 20:20:04.961803

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7bcc18fc765'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('menuler',
    sa.Column('menuno', sa.Integer(), nullable=False),
    sa.Column('menuresmi', sa.String(length=255), nullable=True),
    sa.Column('menuadi', sa.String(length=255), nullable=True),
    sa.Column('menufiyati', sa.String(length=255), nullable=True),
    sa.Column('menutipi', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('menuno')
    )
    op.create_table('slayt',
    sa.Column('slaytno', sa.Integer(), nullable=False),
    sa.Column('slaytfiyati', sa.String(length=50), nullable=True),
    sa.Column('slaytfotosu', sa.String(length=255), nullable=True),
    sa.Column('slaytbas', sa.String(length=255), nullable=True),
    sa.Column('slayttipi', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('slaytno')
    )
    op.create_table('yemekler1',
    sa.Column('no', sa.Integer(), nullable=False),
    sa.Column('yemekİsmi', sa.String(length=50), nullable=True),
    sa.Column('yemekFiyati', sa.String(length=50), nullable=True),
    sa.Column('yemekİcerik', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('no')
    )
    op.create_table('yemekler2',
    sa.Column('yemekno', sa.Integer(), nullable=False),
    sa.Column('yemekİsmi2', sa.String(length=50), nullable=True),
    sa.Column('yemekFiyati2', sa.String(length=50), nullable=True),
    sa.Column('yemekİcerik2', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('yemekno')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('yemekler2')
    op.drop_table('yemekler1')
    op.drop_table('slayt')
    op.drop_table('menuler')
    # ### end Alembic commands ###