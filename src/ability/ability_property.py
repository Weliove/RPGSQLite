from src.connection.handle_items import get_items


def get_items_names():
    items = get_items()
    result = []

    for item in items:
        result.append(item['name'])

    return result


def get_items_ids(items_names):
    result = []
    items = get_items()

    for item in items_names:
        for stored_item in items:
            if item == stored_item['name']:
                item_id = stored_item['id']
                result.append(item_id)

    return result
