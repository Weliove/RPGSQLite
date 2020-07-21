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
    proficiency = convert_array_to_string(entity['proficiency'])
    description = entity['description']

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                       (name, type_, health, adrenaline, 1, '0', 'None', 'None', 'None', proficiency, description))


def get_user_attributes(cursor):
    return [{
        'name': row[0],
        'type': row[1],
        'health': row[2],
        'adrenaline': row[3],
        'class': row[4],
        'items': row[5],
        'physical_ability': row[6],
        'title': row[7],
        'abilities': row[8],
        'proficiency': row[9],
        'description': row[10]
    } for row in cursor.fetchall()][0]


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
            cursor.execute('SELECT name FROM items WHERE type=?', (type_,))
        else:
            cursor.execute('SELECT name FROM items WHERE name=?', (name,))

        entity = get_list(cursor)

    return entity


def convert_array_to_string(items):
    result = ''

    for item in items:
        result += item

    return result


def convert_string_to_array(items):
    return tuple(items.split(','))
