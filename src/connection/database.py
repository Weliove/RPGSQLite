from .database_connection import DatabaseConnection


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


def get_names(cursor):
    return [{'name': row[0]} for row in cursor.fetchall()]


def get_list(cursor):
    return [row[0] for row in cursor.fetchall()]


def get_users_name(type_):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        if type_ == 'Characters, NPCs & Monsters':
            cursor.execute('SELECT name FROM users WHERE type=1')
            characters = get_names(cursor)

            cursor.execute('SELECT name FROM users WHERE type=2')
            npcs = get_names(cursor)

            cursor.execute('SELECT name FROM users WHERE type=3')
            monsters = get_names(cursor)

            result = characters + npcs + monsters
        elif type_ == 'Characters & NPCs':
            cursor.execute('SELECT name FROM users WHERE type=1')
            characters = get_names(cursor)

            cursor.execute('SELECT name FROM users WHERE type=2')
            npcs = get_names(cursor)

            result = characters + npcs
        elif type_ == 'NPCs & Monsters':
            cursor.execute('SELECT name FROM users WHERE type=2')
            npcs = get_names(cursor)

            cursor.execute('SELECT name FROM users WHERE type=3')
            monsters = get_names(cursor)

            result = npcs + monsters
        else:
            cursor.execute('SELECT name FROM users WHERE type=?', (type_,))
            result = get_names(cursor)

    return result


def get_user(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM users WHERE name=?', (name,))
        characters = [{
            'name': row[0],
            'health': row[1],
            'adrenaline': row[2],
            'proficiency': row[3],
            'description': row[4]
        } for row in cursor.fetchall()]

    return characters


def get_entities(db_entity):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'SELECT name FROM {db_entity}')
        entity = get_list(cursor)

    return entity


def get_specific_items(name, type_):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        if name is None:
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
