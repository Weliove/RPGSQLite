from .database_connection import DatabaseConnection


def add_ability(ability, user_name, item_id):
    pass


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


def get_abilities_attributes(cursor):
    return [{
        'id': row[0],
        'name': row[1]
    } for row in cursor.fetchall()]
