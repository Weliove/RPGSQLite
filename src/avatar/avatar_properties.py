from src.connection.database import *
from src.connection.handle_classes import get_classes
from src.connection.handle_items import get_specific_items


def get_avatar_types():
    return tuple(("Character", "NPC", "Monster"))


def get_item_types():
    return ['None']


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


def get_armors():
    return get_specific_items('', 1)


def get_weapons():
    return get_specific_items('', 2)


def get_classes_names():
    classes = get_classes()
    result = []

    for item in classes:
        result.append(item['name'])

    return result


def get_classes_ids(classes_names):
    result = []
    classes = get_classes()

    for class_ in classes_names:
        for stored_class in classes:
            if class_ == stored_class['name']:
                class_id = stored_class['id']
                result.append(class_id)

    return result


def get_proficiencies():
    proficiencies = [
        "Arcanism",
        "Manufacturing",
        "Athletics",
        "Occult",
        "Medicine",
        "Nature",
        "Survival",
        "Stealth",
        "Religion",
        "Society",
        "Intimidation",
        "Logia",
        "Diplomacy",
        "Concealment"
    ]
    result = sorted(proficiencies)
    result.insert(0, "None")

    return result
