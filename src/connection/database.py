import sqlite3

from .database_connection import DatabaseConnection
from .handle_users import get_user_attributes


def get_list(cursor):
    return [row[0] for row in cursor.fetchall()]


search_database = {
    # users
    'Character': 'users',
    'NPC': 'users',
    'Monster': 'users',
    # items
    'Armor': 'items',
    'Weapon': 'items',
    # others
    'Title': 'titles',
    'Ability': 'abilities',
    'Wiki': 'wiki'
}

search_types = {
    'Character': 1,
    'NPC': 2,
    'Monster': 3,
    'Armor': 1,
    'Weapon': 2,
    'Title': None,
    'Ability': None,
    'Wiki': None
}


def get_entity(name, type_):
    db_entity = search_database[type_]
    db_type = search_types[type_]

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'SELECT * FROM {db_entity} WHERE name=?', (name,))
        if db_entity == 'users':
            entity = get_user_attributes(cursor)

    return entity


def get_entity_name_by_id(id_, db_entity):
    if id_ == 0:
        return 'None'

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'SELECT name FROM {db_entity} WHERE id=?', (id_,))
        entity = get_list(cursor)

    return entity


# --- OTHERS ---
def get_search_entities(name, type_):
    entity_name = name.lower()
    db_entity = search_database[type_]
    db_type = search_types[type_]

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        if entity_name == '' or entity_name == '*':
            if db_entity == 'users' or db_entity == 'items':
                cursor.execute(f'SELECT name FROM {db_entity} WHERE type=?', (db_type,))
                entity = get_list(cursor)
            else:
                cursor.execute(f'SELECT name FROM {db_entity}')
                entity = get_list(cursor)
        else:
            if db_entity == 'users' or db_entity == 'items':
                cursor.execute(f'SELECT name FROM {db_entity} WHERE name LIKE ? AND type=? ORDER BY name',
                               ('%' + entity_name + '%', db_type))
                entity = get_list(cursor)
            else:
                cursor.execute(f'SELECT name FROM {db_entity} WHERE name LIKE ? ORDER BY name',
                               ('%' + entity_name + '%',))
                entity = get_list(cursor)

    return entity


def convert_list_to_string(items):
    if len(items) == 0:
        return 'None'

    result = ','.join(map(str, items))
    return result


def convert_string_to_array(items):
    return tuple(items.split(','))
