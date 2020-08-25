import tkinter as tk
from tkinter import ttk

from src.avatar.avatar import Avatar
from src.connection.handle_users import get_user_classes, get_user_items, get_user_abilities, get_user_proficiencies
from src.interface.interface_functions import button_state, generate_classes, generate_items, generate_abilities, \
    generate_proficiencies


class UserInterface(ttk.Frame):
    def __init__(self, container, entity, type_, show_search, show_home, show_interface_verification):
        super().__init__(container)

        self.item_types = {1: 'Armor', 2: 'Weapon'}

        self.name = entity['name']
        self.type_ = entity['type']
        self.health = 'Health:  ' + entity['health']
        self.adrenaline = 'Adrenaline:  ' + entity['adrenaline']
        self.class_ = get_user_classes(self.name)
        self.items = get_user_items(self.name)
        self.physical_ability = 'Physical Ability:  ' + entity['physical_ability']
        self.titles = 'Titles:  None'  # 'Titles:  ' + entity['title']
        self.abilities = get_user_abilities(self.name)
        self.proficiency = get_user_proficiencies(self.name)
        self.description = 'Description:  ' + entity['description']

        self.avatar = Avatar(self.name, self.type_, self.health, self.adrenaline, self.class_, self.items,
                             self.physical_ability, self.titles, self.abilities, self.proficiency, self.description)

        self.create_widgets()

        self.create_buttons(show_search, show_home, show_interface_verification)

    def create_widgets(self):
        name = ttk.Label(
            self,
            text=self.name
        )
        name.grid(row=0, column=0, sticky="EW")

        name_separator = ttk.Separator(
            self
        )
        name_separator.grid(row=1, column=0, columnspan=1, sticky="EW")

        health = ttk.Label(
            self,
            text=self.health
        )
        health.grid(row=2, column=0, sticky="EW")

        adrenaline = ttk.Label(
            self,
            text=self.adrenaline
        )
        adrenaline.grid(row=3, column=0, sticky="NSEW")

        class_ = ttk.Label(
            self,
            text=generate_classes(self.class_)
        )
        class_.grid(row=4, column=0, sticky="NSEW")

        items = ttk.Label(
            self,
            text=generate_items(self.items, self.item_types)
        )
        items.grid(row=5, column=0, sticky="NSEW")

        physical_ability = ttk.Label(
            self,
            text=self.physical_ability
        )
        physical_ability.grid(row=6, column=0, sticky="NSEW")

        title = ttk.Label(
            self,
            text=self.titles
        )
        title.grid(row=7, column=0, sticky="NSEW")

        abilities = ttk.Label(
            self,
            text=generate_abilities(self.abilities)
        )
        abilities.grid(row=8, column=0, sticky="NSEW")

        proficiency = ttk.Label(
            self,
            text=generate_proficiencies(self.proficiency)
        )
        proficiency.grid(row=9, column=0, sticky="NSEW")

        description = ttk.Label(
            self,
            text=self.description
        )
        description.grid(row=10, column=0, sticky="NSEW")

        def reconfigure_labels(event):
            physical_ability.configure(wraplength=self.winfo_width() - 25)
            items.configure(wraplength=self.winfo_width() - 25)
            title.configure(wraplength=self.winfo_width() - 25)
            abilities.configure(wraplength=self.winfo_width() - 25)
            proficiency.configure(wraplength=self.winfo_width() - 25)
            description.configure(wraplength=self.winfo_width() - 25)

        self.bind("<Configure>", reconfigure_labels)

    def create_buttons(self, show_search, show_home, show_interface_verification):
        items_button = ttk.Button(
            self,
            text="Verify Items",
            command=lambda: show_interface_verification(self.items, 'Item'),
            state=button_state(self.items),
            cursor="hand2"
        )
        items_button.grid(column=0, sticky="EW")

        abilities_button = ttk.Button(
            self,
            text="Verify Abilities",
            command=lambda: show_interface_verification(self.abilities, 'Ability'),
            state=button_state(self.abilities),
            cursor="hand2"
        )
        abilities_button.grid(column=0, sticky="EW")

        back_button = ttk.Button(
            self,
            text="← Back",
            command=show_search,
            cursor="hand2"
        )
        back_button.grid(column=0, sticky="EW")

        home_button = ttk.Button(
            self,
            text="Home",
            command=show_home,
            cursor="hand2"
        )
        home_button.grid(column=0, sticky="EW")
