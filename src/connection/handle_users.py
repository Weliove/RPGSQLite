import sqlite3

from .database_connection import DatabaseConnection

from .handle_classes import get_classes_attributes

from .handle_items import get_items_attributes


def get_list(cursor):
    return [row[0] for row in cursor.fetchall()]


# --- USERS ---
def add_user(entity):
    name = entity['name']
    type_ = entity['type']
    health = entity['health']
    adrenaline = entity['adrenaline']
    physical_ability = entity['physical_ability']
    description = entity['description']

    classes_id = entity['class']
    items_id = entity['items']
    titles_id = entity['titles']
    abilities_id = entity['abilities']
    proficiencies_id = entity['proficiency']

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)',
                       (name, type_, health, adrenaline, physical_ability, description))

        if len(classes_id) > 0:
            for class_ in classes_id:
                cursor.execute('INSERT INTO users_classes (class_id, user_name) VALUES (?, ?)', (class_, name))

        if len(items_id) > 0:
            for item in items_id:
                cursor.execute('INSERT INTO users_items (item_id, user_name) VALUES (?, ?)', (item, name))

        if len(titles_id) > 0:
            for title in titles_id:
                cursor.execute('INSERT INTO users_titles (title_id, user_name) VALUES (?, ?)', (title, name))

        if len(abilities_id) > 0:
            for ability in abilities_id:
                cursor.execute('INSERT INTO users_abilities (ability_id, user_name) VALUES(?, ?)', (ability, name))

        if len(proficiencies_id) > 0:
            for proficiency in proficiencies_id:
                cursor.execute('INSERT INTO users_proficiencies (proficiency_id, user_name) VALUES (?, ?)',
                               (proficiency, name))


def get_users_name(name, type_):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        if name == '':
            cursor.execute('SELECT name FROM users WHERE type=?', (type_,))
            result = get_list(cursor)
        else:
            cursor.execute('SELECT name FROM users WHERE name=? AND type=?', (name, type_))
            result = get_list(cursor)

    return result


def get_user(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM users WHERE name=?', (name,))
        characters = get_user_attributes(cursor)

    return characters


def get_user_attributes(cursor):
    return [{
        'name': row[0],
        'type': row[1],
        'health': row[2],
        'adrenaline': row[3],
        'physical_ability': row[4],
        'description': row[5]
    } for row in cursor.fetchall()][0]


def get_user_classes(user_name):
    classes = []

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT class_id FROM users_classes WHERE user_name=?', (user_name,))
        classes_id = get_list(cursor)

        for class_id in classes_id:
            cursor.execute('SELECT * FROM classes WHERE id=?', (class_id,))
            classes += get_classes_attributes(cursor)

    return classes


def get_user_items(user_name):
    items = []

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT item_id FROM users_items WHERE user_name=?', (user_name,))
        items_id = get_list(cursor)

        for item in items_id:
            cursor.execute('SELECT * FROM items WHERE id=?', (item,))
            items += get_items_attributes(cursor)

    return items


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


def get_user_types():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'SELECT * FROM users_types')

        entity = get_user_types_attributes(cursor)

    return entity


def get_user_types_attributes(cursor):
    return [{
        'id': row[0],
        'name': row[1]
    } for row in cursor.fetchall()]


def get_user_abilities(cursor):
    pass


def get_user_proficiencies(cursor):
    pass


def get_user_titles(cursor):
    pass
