from src.connection.handle_abilities import get_abilities


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
    if entity == 'ability':
        return get_abilities()
    else:
        return None
