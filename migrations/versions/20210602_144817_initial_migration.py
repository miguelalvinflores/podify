"""initial migration

Revision ID: 96eb10c5e1ed
Revises: 
Create Date: 2021-06-02 14:48:17.642827

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96eb10c5e1ed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_name', sa.String(length=200), nullable=False),
    sa.Column('image_url', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('profile_pic_url', sa.String(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('albums',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('album_title', sa.String(length=200), nullable=False),
    sa.Column('image_url', sa.String(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tracks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('song_title', sa.String(length=200), nullable=False),
    sa.Column('image_url', sa.String(), nullable=False),
    sa.Column('source_url', sa.String(), nullable=False),
    sa.Column('album_id', sa.Integer(), nullable=True),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['album_id'], ['albums.id'], ),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tracks')
    op.drop_table('albums')
    op.drop_table('users')
    op.drop_table('artists')
    # ### end Alembic commands ###
