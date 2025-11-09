import click
from flask import current_app
from app.db.raw_connection import connect

from sqlalchemy.exc import SQLAlchemyError
from app.db.models import Base
from app.db.orm_connection import engine


@click.command('init-db')
def init_db_command():
    conn = connect()
    with conn.cursor() as cursor:
        with current_app.open_resource('db/schema.sql') as f:
            cursor.execute(f.read())
    conn.commit()
    click.echo('Initialized the database ...')


@click.command('init-db-orm')
def init_db_orm_command():
    try:
        from app.db import models

        Base.metadata.create_all(bind=engine)
        click.echo('ORM. Initialized the database...')
    except SQLAlchemyError as e:
        click.echo(f'Error initializing the database: {e}')


def init_commands(app):
    app.cli.add_command(init_db_command)
    app.cli.add_command(init_db_orm_command)
