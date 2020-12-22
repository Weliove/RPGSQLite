from src.connection.handle_proficiencies import add_proficiency, update_proficiency


class Proficiency:
    def __init__(self, name, description, topics):
        self.name = name
        self.description = description
        self.topics = topics

        self.proficiency = {
            'name': self.name,
            'description': self.description,
            'topics': self.topics
        }

    def create_proficiency(self):
        return add_proficiency(self.proficiency)

    def update_proficiency(self, current_name):
        return update_proficiency(self.proficiency, current_name)
