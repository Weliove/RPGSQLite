from src.connection.handle_abilities import add_ability


class Ability:
    def __init__(self, name, user, type_, casting, components, requirements, conditions, effects, description):
        self.name = name
        self.user = user
        self.type_ = type_
        self.casting = casting
        self.components = components
        self.requirements = requirements
        self.conditions = conditions
        self.effects = effects
        self.description = description

        self.ability = {
            'name': self.name,
            'casting': self.casting,
            'components': self.components,
            'requirements': self.requirements,
            'conditions': self.conditions,
            'effects': self.effects,
            'description': self.description
        }

    def add_ability(self):
        return add_ability(self.ability, self.user)
