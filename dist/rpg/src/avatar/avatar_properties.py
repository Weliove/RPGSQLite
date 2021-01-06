from src.connection.handle_abilities import get_abilities, get_abilities_name_by_type
from src.connection.handle_classes import get_classes
from src.connection.handle_items import get_specific_items
from src.connection.handle_proficiencies import get_proficiencies
from src.connection.handle_titles import get_titles
from src.connection.handle_users import get_user_types


def get_entities_names(entities: list) -> list:
    return [entity['name'] for entity in entities]


def get_entities_ids(entities: list, entities_names: list) -> list:
    result = []

    for entity_name in entities_names:
        for entity in entities:
            if entity_name == entity['name']:
                entity_id = entity['id']
                result.append(entity_id)

    return result


def get_user_types_ids(type_name: str) -> int:
    type_result = -1
    types = get_user_types()

    print(types)

    for stored_type in types:
        if stored_type['name'] == type_name:
            type_result = stored_type['id']
            break

    return type_result
