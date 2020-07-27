import sqlite3

from .database_connection import DatabaseConnection


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


# --- USERS ---
def add_user(entity):
    name = entity['name']
    type_ = entity['type']
    health = entity['health']
    adrenaline = entity['adrenaline']
    class_ = entity['class']
    physical_ability = entity['physical_ability']
    description = entity['description']

    items_id = entity['items']
    titles_id = entity['titles']
    abilities_id = entity['abilities']
    proficiencies_id = entity['proficiency']

    print(items_id)
    print(titles_id)
    print(abilities_id)
    print(proficiencies_id)

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        try:
            cursor.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)',
                           (name, type_, health, adrenaline, class_, physical_ability, description))

            if len(items_id) > 0:
                for item in items_id:
                    cursor.execute('INSERT INTO users_items(item_id, user_name) VALUES (?, ?)', (item, name))

            if len(titles_id) > 0:
                for title in titles_id:
                    cursor.execute('INSERT INTO users_titles(title_id, user_name) VALUES (?, ?)', (title, name))

            if len(abilities_id) > 0:
                for ability in abilities_id:
                    cursor.execute('INSERT INTO users_abilities(ability_id, user_name) VALUES(?, ?)', (ability, name))

            if len(proficiencies_id) > 0:
                for proficiency in proficiencies_id:
                    cursor.execute('INSERT INTO users_proficiencies(proficiency_id, user_name) VALUES (?, ?)',
                                   (proficiency, name))
        except sqlite3.Error as error:
            return error


def get_user_abilities(cursor):
    pass


def get_user_proficiencies(cursor):
    pass


def get_user_titles(cursor):
    pass


def get_users_name(name, type_):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        if name == '':
            cursor.execute('SELECT name FROM users WHERE type=?', (type_,))
            result = get_list(cursor)
        else:
            cursor.execute('SELECT name FROM users WHERE name=?', (name,))
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
        'class': row[4],
        'physical_ability': row[5],
        'description': row[6]
    } for row in cursor.fetchall()][0]


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


def get_items_attributes(cursor):
    return [{
        'id': row[0],
        'name': row[1]
    } for row in cursor.fetchall()]


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


def get_specific_items(name, type_):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        if name == '':
            cursor.execute('SELECT * FROM items WHERE type=?', (type_,))
        else:
            cursor.execute('SELECT * FROM items WHERE name=?', (name,))

        entity = get_items_attributes(cursor)

    return entity


# --- CLASSES ---
def get_classes():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'SELECT * FROM classes')

        entity = get_classes_attributes(cursor)

    return entity


def get_classes_attributes(cursor):
    return [{
        'id': row[0],
        'name': row[1],
    } for row in cursor.fetchall()]


def convert_list_to_string(items):
    if len(items) == 0:
        return 'None'

    result = ','.join(map(str, items))
    return result


def convert_string_to_array(items):
    return tuple(items.split(','))
