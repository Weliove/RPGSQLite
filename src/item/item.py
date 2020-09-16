from src.connection.handle_items import add_item, update_item


class Item:
    def __init__(self, name, type_, reduction, damage, range_, health, area, abilities, effects, description,
                 user=None):
        self.name = name
        self.type_ = type_
        self.reduction = reduction
        self.damage = damage
        self.range_ = range_
        self.health = health
        self.area = area
        self.abilities = abilities
        self.effects = effects
        self.description = description
        self.user = user

        self.item = {
            'name': self.name,
            'type': self.type_,
            'reduction': self.reduction,
            'damage': self.damage,
            'range': self.range_,
            'health': self.health,
            'area': self.area,
            'abilities': self.abilities,
            'effects': self.effects,
            'description': self.description
        }

    def create_item(self):
        return add_item(self.item, self.user)

    def update_item(self, id_):
        return update_item(self.item, id_)
