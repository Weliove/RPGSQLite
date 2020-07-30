import sqlite3

from .database_connection import DatabaseConnection


def add_item(item, user_name):
    name = item['name']
    type_ = item['type']
    reduction = item['reduction']
    damage = item['damage']
    range_ = item['range']
    health = item['health']
    area = item['area']
    effects = item['effects']
    description = item['description']

    abilities_id = item['abilities']

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        try:
            cursor.execute('INSERT INTO items VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                           (name, type_, reduction, damage, range_, health, area, effects, description))

            item_id = cursor.lastrowid

            if len(abilities_id) > 0:
                for ability in abilities_id:
                    cursor.execute('INSERT INTO items_abilities (ability_id, item_id)', (ability, item_id))

            if user_name != 'None':
                cursor.execute('INSERT INTO users_items (item_id, user_name)', (item_id, user_name))
        except sqlite3.Error as error:
            return error


def get_items_attributes(cursor):
    return [{
        'id': row[0],
        'name': row[1]
    } for row in cursor.fetchall()]


def get_specific_items(name, type_):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        if name == '':
            cursor.execute('SELECT * FROM items WHERE type=?', (type_,))
        else:
            cursor.execute('SELECT * FROM items WHERE name=?', (name,))

        entity = get_items_attributes(cursor)

    return entity
