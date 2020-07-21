import tkinter as tk
from tkinter import ttk

from src.connection.database import get_entity_name_by_id, convert_array_to_string


class UserInterface(ttk.Frame):
    def __init__(self, container, entity, type_, show_home):
        super().__init__(container)

        self.name = 'Name:  ' + entity['name']
        self.health = 'Health:  ' + entity['health']
        self.adrenaline = 'Adrenaline:  ' + entity['adrenaline']
        self.class_ = 'Class:  ' + convert_array_to_string(get_entity_name_by_id(entity['class'], 'classes'))
        self.items = 'Items:  ' + entity['items']
        self.physical_ability = 'Physical Ability:  ' + entity['physical_ability']
        self.title = 'Titles:  ' + entity['title']
        self.abilities = 'Abilities:  ' + entity['abilities']
        self.proficiency = 'Proficiencies:  ' + entity['proficiency']
        self.description = 'Description:  ' + entity['description']

        self.create_widgets(entity)

        self.create_buttons(show_home)

    def create_widgets(self, entity):
        print(entity)
        name = ttk.Label(
            self,
            text=self.name
        )
        name.grid(row=0, column=0, sticky="NSEW")

        health = ttk.Label(
            self,
            text=self.health
        )
        health.grid(row=1, column=0, sticky="NSEW")

        adrenaline = ttk.Label(
            self,
            text=self.adrenaline
        )
        adrenaline.grid(row=2, column=0, sticky="NSEW")

        class_ = ttk.Label(
            self,
            text=self.class_
        )
        class_.grid(row=3, column=0, sticky="NSEW")

        items = ttk.Label(
            self,
            text=self.items
        )
        items.grid(row=4, column=0, sticky="NSEW")

        physical_ability = ttk.Label(
            self,
            text=self.physical_ability
        )
        physical_ability.grid(row=5, column=0, sticky="NSEW")

        title = ttk.Label(
            self,
            text=self.title
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

    def create_buttons(self, show_home):
        back_button = ttk.Button(
            self,
            text="← Back",
            command=show_home,
            cursor="hand2"
        )
        back_button.grid(column=0, sticky="EW")
