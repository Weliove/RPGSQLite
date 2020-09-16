from .database import *
from .database import DatabaseConnection


def add_ability(ability, user):
    name = ability['name']
    type_ = ability['type']
    casting = ability['casting']
    components = ability['components']
    requirements = ability['requirements']
    conditions = ability['conditions']
    effects = ability['effects']
    description = ability['description']

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO abilities (name, type, casting, components, requirements, conditions, effects, '
                       'description) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                       (name, type_, casting, components, requirements, conditions, effects, description))

        ability_id = cursor.lastrowid

        if user != 'Character' and user != 'NPC' and user != 'Monster' and (type_ == 1 or type_ == 2 or type_ == 3):
            cursor.execute('INSERT INTO users_abilities (ability_id, user_name) VALUES (?, ?)', (ability_id, user))
        elif user != 'Item' and type_ == 4:
            item = get_specific_items(user, 0)[0]
            item_id = item['id']
            cursor.execute('INSERT INTO items_abilities (ability_id, item_id) VALUES (?, ?)', (ability_id, item_id))


def get_abilities():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'SELECT * FROM abilities')

        entity = get_abilities_attributes(cursor)

    return entity


def get_abilities_by_id(ability_id):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'SELECT * FROM abilities WHERE id=?', (ability_id,))

        entity = get_abilities_attributes(cursor)

    return entity


def get_abilities_name_by_type(ability_type):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'SELECT name FROM abilities WHERE type=?', (ability_type,))

        entity = get_list(cursor)

    return entity


def get_list(cursor):
    return [row[0] for row in cursor.fetchall()]


def get_abilities_attributes(cursor):
    return [{
        'id': row[0],
        'name': row[1],
        'type': row[2],
        'casting': row[3],
        'components': row[4],
        'requirements': row[5],
        'conditions': row[6],
        'effects': row[7],
        'description': row[8]
    } for row in cursor.fetchall()]


def get_ability_attributes(cursor):
    return [{
        'id': row[0],
        'name': row[1],
        'type': row[2],
        'casting': row[3],
        'components': row[4],
        'requirements': row[5],
        'conditions': row[6],
        'effects': row[7],
        'description': row[8]
    } for row in cursor.fetchall()][0]