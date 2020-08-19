from .database import *
from .database import DatabaseConnection


def get_titles():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'SELECT * FROM titles')

        entity = get_titles_attributes(cursor)

    return entity


def get_titles_attributes(cursor):
    return [{
        'id': row[0],
        'name': row[1]
    } for row in cursor.fetchall()]
