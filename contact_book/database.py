import sqlite3
from typing import Optional


def create_table(conn: sqlite3.Connection) -> None:

    with conn:
        conn.execute(
            """ CREATE TABLE IF NOT EXISTS contacts (
                id integer PRIMARY KEY,
                name text NOT NULL,
                address text NOT NULL,
                phone text NOT NULL,
                email text NOT NULL
            );"""
        )


def create_database_connection(path: str) -> Optional[sqlite3.Connection]:
    """Creates database connection to sqlite database in the path.
    
    Parameters
    ------------
    path: str
        path to the file where the database should reside

    Returns
    ------------
    Optional[sqlite3.Connection]
        sqlite connection, None if connection failed
    """

    conn = None
    try:
        conn = sqlite3.connect(path)
        create_table(conn)
    except Exception as e:
        print(e)
    return conn
