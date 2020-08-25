from src.connection.handle_titles import add_title


class Title:
    def __init__(self, name, users, requirements, description):
        self.name = name
        self.users = users
        self.description = description
        self.requirements = requirements

        self.title = {
            'name': self.name,
            'requirements': self.requirements,
            'description': self.description
        }

    def create_title(self):
        return add_title(self.title, self.users)

    def update_title(self):
        pass
