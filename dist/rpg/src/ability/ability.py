from src.connection.handle_abilities import add_ability, update_ability


class Ability:
    def __init__(self, name, casting, components, requirements, conditions, effects, description, type_=None,
                 user=None):
        self.name = name
        self.casting = casting
        self.components = components
        self.requirements = requirements
        self.conditions = conditions
        self.effects = effects
        self.description = description
        self.type_ = type_
        self.user = user

        self.ability = {
            'name': self.name,
            'type': self.type_,
            'casting': self.casting,
            'components': self.components,
            'requirements': self.requirements,
            'conditions': self.conditions,
            'effects': self.effects,
            'description': self.description
        }

    def create_ability(self):
        return add_ability(self.ability, self.user)

    def update_ability(self, id_):
        return update_ability(self.ability, id_)
