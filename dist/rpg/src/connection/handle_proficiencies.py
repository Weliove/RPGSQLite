from .database import *
from .database import DatabaseConnection


def get_proficiencies():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'SELECT * FROM proficiencies')

        entity = get_proficiencies_attributes(cursor)

    return entity


def get_proficiencies_attributes(cursor):
    return [{
        'id': row[0],
        'name': row[1]
    } for row in cursor.fetchall()]


def get_proficiencies_by_id(proficiency_id):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'SELECT * FROM proficiencies WHERE id=?', (proficiency_id,))

        proficiency = get_proficiencies_attributes(cursor)

    return proficiency