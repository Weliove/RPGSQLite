from src.connection.database import *


def get_avatar_type():
    types = sorted(("Character", "Npc", "Monster"))
    return sorted(types)


def get_item_types():
    return get_entities('items_types')


def get_special_armors():
    return get_specific_items(None, 1)


def get_special_weapons():
    return get_specific_items(None, 2)


def get_avatar_classes():
    classes = [
        "Warrior",
        "Thief",
        "Guardian",
        "Reaper",
        "Support",
        "Esper"
    ]
    result = sorted(classes)
    result.insert(0, "None")

    return result


def get_armors():
    armors = (
        "None",
        "Rank 1",
        "Rank 2",
        "Rank 3",
        "Rank 4",
        "Rank 5"
    )
    return armors


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
