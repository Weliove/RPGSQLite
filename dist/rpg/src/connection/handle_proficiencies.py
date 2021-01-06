from .database import *
from .database import DatabaseConnection


def add_proficiency(proficiency):
    proficiency_name = proficiency['name']
    proficiency_description = proficiency['description']

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        for level in range(5):
            proficiency_level = ' ' + str(level + 1)
            cursor.execute('INSERT INTO proficiencies (name, description) VALUES (?, ?)',
                           (proficiency_name + proficiency_level, proficiency_description))


def update_proficiency(proficiency, current_name):
    pass


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
