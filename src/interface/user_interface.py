import tkinter as tk
from tkinter import ttk

from src.avatar.avatar import Avatar
from src.connection.database import get_entity_name_by_id, convert_list_to_string
from src.connection.handle_users import get_user_classes, get_user_items


class UserInterface(ttk.Frame):
    def __init__(self, container, entity, type_, show_home):
        super().__init__(container)

        self.name = entity['name']
        self.type_ = entity['type']
        self.health = 'Health:  ' + entity['health']
        self.adrenaline = 'Adrenaline:  ' + entity['adrenaline']
        self.class_ = get_user_classes(self.name)
        self.items = get_user_items(self.name)
        self.physical_ability = 'Physical Ability:  ' + entity['physical_ability']
        self.titles = 'Titles:  None'  # 'Titles:  ' + entity['title']
        self.abilities = 'Abilities:  None'  # 'Abilities:  ' + entity['abilities']
        self.proficiency = 'Proficiencies:  None'  # 'Proficiencies:  ' + entity['proficiency']
        self.description = 'Description:  ' + entity['description']

        self.avatar = Avatar(self.name, self.type_, self.health, self.adrenaline, self.class_, self.items,
                             self.physical_ability, self.titles, self.abilities, self.proficiency, self.description)

        self.create_widgets(entity)

        self.create_buttons(show_home)

    def create_widgets(self, entity):
        print(entity)
        name = ttk.Label(
            self,
            text='Name:  ' + self.name
        )
        name.grid(row=0, column=0, sticky="EW")

        health = ttk.Label(
            self,
            text=self.health
        )
        health.grid(row=1, column=0, sticky="EW")

        adrenaline = ttk.Label(
            self,
            text=self.adrenaline
        )
        adrenaline.grid(row=2, column=0, sticky="NSEW")

        class_ = ttk.Label(
            self,
            text=self.generate_classes(self.class_)
        )
        class_.grid(row=3, column=0, sticky="NSEW")

        items = ttk.Label(
            self,
            text=self.generate_items(self.items)
        )
        items.grid(row=4, column=0, sticky="NSEW")

        physical_ability = ttk.Label(
            self,
            text=self.physical_ability
        )
        physical_ability.grid(row=5, column=0, sticky="NSEW")

        title = ttk.Label(
            self,
            text=self.titles
        )
        title.grid(row=6, column=0, sticky="NSEW")

        abilities = ttk.Label(
            self,
            text=self.abilities
        )
        abilities.grid(row=7, column=0, sticky="NSEW")

        proficiency = ttk.Label(
            self,
            text=self.proficiency
        )
        proficiency.grid(row=8, column=0, sticky="NSEW")

        description = ttk.Label(
            self,
            text=self.description
        )
        description.grid(row=9, column=0, sticky="NSEW")

    def generate_items(self, items):
        text = 'Items:'

        if len(items) == 0:
            return text + ' None'

        text += '\n'

        for item in items:
            text += '\t' + item['name'] + '\n\n'

        return text

    def generate_classes(self, classes):
        text = 'Classes:'

        if len(classes) == 0:
            return text + ' None'

        text += '\n'

        for class_ in classes:
            text += '\t' + class_['name'] + '\n\n'

        return text

    def create_buttons(self, show_home):
        back_button = ttk.Button(
            self,
            text="← Back",
            command=show_home,
            cursor="hand2"
        )
        back_button.grid(column=0, sticky="EW")
