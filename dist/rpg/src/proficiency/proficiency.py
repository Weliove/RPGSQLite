from src.connection.handle_proficiencies import add_proficiency, update_proficiency


class Proficiency:
    def __init__(self, name, description):
        self.name = name
        self.description = description

        self.proficiency = {
            'name': self.name,
            'description': self.description
        }

    def create_proficiency(self) -> bool:
        return add_proficiency(self.proficiency)

    def update_proficiency(self, id_):
        return update_proficiency(self.proficiency, id_)
