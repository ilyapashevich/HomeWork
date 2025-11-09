from psycopg2 import pool
from flask import g

from app.config import DATABASE_CONFIG


connection_pool = pool.SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    **DATABASE_CONFIG
)


def connect():
    if 'db_conn' not in g:
        g.db_conn = connection_pool.getconn()
    return g.db_conn


def close_connection(exception):
    db_conn = g.pop('db_conn', None)
    if db_conn:
        connection_pool.putconn(db_conn)
