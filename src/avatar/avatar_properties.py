from src.connection.handle_abilities import get_abilities, get_abilities_name_by_type
from src.connection.handle_classes import get_classes
from src.connection.handle_items import get_specific_items
from src.connection.handle_proficiencies import get_proficiencies
from src.connection.handle_titles import get_titles
from src.connection.handle_users import get_user_types


def get_avatar_types():
    return tuple(("Character", "NPC", "Monster"))


def get_items(type_):
    items = get_specific_items('', type_)
    result = []

    for item in items:
        result.append(item['name'])

    return result


def get_items_ids(items_names, type_):
    result = []
    items = get_specific_items('', type_)

    for item in items_names:
        for stored_item in items:
            if item == stored_item['name']:
                item_id = stored_item['id']
                result.append(item_id)

    return result


def get_classes_names():
    classes = get_classes()
    result = []

    for item in classes:
        result.append(item['name'])

    return result


def get_entity_ids(entity_type, entities_names):
    result = []
    entities = select_entity(entity_type)

    for entity in entities_names:
        for stored_entities in entities:
            if entity == stored_entities['name']:
                entity_id = stored_entities['id']
                result.append(entity_id)

    return result


def select_entity(entity):
    if entity == 'class':
        return get_classes()
    elif entity == 'proficiency':
        return get_proficiencies()
    elif entity == 'title':
        return get_titles()
    elif entity == 'ability':
        return get_abilities()
    else:
        return None


def get_user_types_ids(type_name):
    type_result = -1
    types_ = get_user_types()

    print(types_)

    for stored_type in types_:
        if stored_type['name'] == type_name:
            type_result = stored_type['id']

    return type_result
