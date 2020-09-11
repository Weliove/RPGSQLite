from src.connection.handle_users import add_user, update_user


class Avatar:
    def __init__(self, name, type_, health, adrenaline, class_, items, physical_ability, titles, abilities,
                 proficiency, description):
        self.name = name
        self.type_ = type_
        self.health = health
        self.adrenaline = adrenaline
        self.class_ = class_
        self.items = items
        self.physical_ability = physical_ability
        self.titles = titles
        self.abilities = abilities
        self.proficiency = proficiency
        self.description = description

        self.avatar = {
            'name': self.name,
            'type': self.type_,
            'health': self.health,
            'adrenaline': self.adrenaline,
            'class': self.class_,
            'items': self.items,
            'physical_ability': self.physical_ability,
            'titles': self.titles,
            'abilities': self.abilities,
            'proficiency': self.proficiency,
            'description': self.description
        }

    def create_character(self):
        return add_user(self.avatar)

    def update_user(self, current_name):
        return update_user(self.avatar, current_name)
