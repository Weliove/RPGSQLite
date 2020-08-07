from .database_connection import DatabaseConnection


def get_abilities():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'SELECT * FROM abilities')

        entity = get_abilities_attributes(cursor)

    return entity


def get_abilities_attributes(cursor):
    return [{
        'id': row[0],
        'name': row[1]
    } for row in cursor.fetchall()]
