from .database import *
from .database import DatabaseConnection


def add_title(title, users_names):
    name = title['name']
    description = title['description']
    requirements = title['requirements']

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO titles (name, description, requirements) VALUES (?, ?, ?)',
                       (name, description, requirements))

        title_id = cursor.lastrowid

        if len(users_names) > 0:
            for user_name in users_names:
                cursor.execute('INSERT INTO users_titles (title_id, user_name) VALUES (?, ?)', (title_id, user_name))


def get_titles():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'SELECT * FROM titles')

        entity = get_titles_attributes(cursor)

    return entity


def get_titles_attributes(cursor):
    return [{
        'id': row[0],
        'name': row[1],
        'description': row[2],
        'requirements': row[3]
    } for row in cursor.fetchall()]