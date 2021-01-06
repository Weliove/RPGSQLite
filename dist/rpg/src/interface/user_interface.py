import tkinter as tk
from tkinter import ttk

from src.avatar.avatar import Avatar
from src.connection.handle_users import get_user_classes, get_user_items, get_user_abilities, get_user_proficiencies, \
    get_user_titles
from src.interface.interface_functions import button_state, generate_classes, generate_items, generate_abilities, \
    generate_proficiencies, generate_titles


class UserInterface(ttk.Frame):
    def __init__(self, container, entity, type_, show_search, show_home, show_edit, show_interface_verification,
                 search_entities_name, search_type):
        super().__init__(container)

        self.entity = entity
        self.entity_type = type_

        self.search_entities_name = search_entities_name
        self.search_type = search_type

        self.item_types = {1: 'Armor', 2: 'Weapon'}

        self.name = entity['name']
        self.type_ = entity['type']
        self.strength_lv = f'Strength Level:  {entity["strength_lv"]}'
        self.magic_lv = f'Magic Level:  {entity["magic_lv"]}'
        self.health = 'Health:  ' + entity['health']
        self.adrenaline = 'Adrenaline:  ' + entity['adrenaline']
        self.class_ = get_user_classes(self.name)
        self.items = get_user_items(self.name)
        self.physical_ability = 'Physical Ability:  ' + entity['physical_ability']
        self.titles = get_user_titles(self.name)
        self.abilities = get_user_abilities(self.name)
        self.proficiency = get_user_proficiencies(self.name)
        self.description = 'Description:  ' + entity['description']

        self.avatar = Avatar(self.name, self.type_, self.strength_lv, self.magic_lv, self.health, self.adrenaline,
                             self.class_, self.items, self.physical_ability, self.titles, self.abilities,
                             self.proficiency, self.description)

        self.create_widgets()

        self.create_buttons(show_search, show_home, show_edit, show_interface_verification)

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

        strength_lv = ttk.Label(
            self,
            text=self.strength_lv
        )
        strength_lv.grid(row=2, column=0, sticky='EW')

        magic_lv = ttk.Label(
            self,
            text=self.magic_lv
        )
        magic_lv.grid(row=3, column=0, sticky='EW')

        health = ttk.Label(
            self,
            text=self.health
        )
        health.grid(row=4, column=0, sticky="EW")

        adrenaline = ttk.Label(
            self,
            text=self.adrenaline
        )
        adrenaline.grid(row=5, column=0, sticky="NSEW")

        class_ = ttk.Label(
            self,
            text=generate_classes(self.class_)
        )
        class_.grid(row=6, column=0, sticky="NSEW")

        items = ttk.Label(
            self,
            text=generate_items(self.items, self.item_types)
        )
        items.grid(row=7, column=0, sticky="NSEW")

        physical_ability = ttk.Label(
            self,
            text=self.physical_ability
        )
        physical_ability.grid(row=8, column=0, sticky="NSEW")

        title = ttk.Label(
            self,
            text=generate_titles(self.titles)
        )
        title.grid(row=9, column=0, sticky="NSEW")

        abilities = ttk.Label(
            self,
            text=generate_abilities(self.abilities)
        )
        abilities.grid(row=10, column=0, sticky="NSEW")

        proficiency = ttk.Label(
            self,
            text=generate_proficiencies(self.proficiency)
        )
        proficiency.grid(row=11, column=0, sticky="NSEW")

        description = ttk.Label(
            self,
            text=self.description
        )
        description.grid(row=12, column=0, sticky="NSEW")

        def reconfigure_labels(event):
            physical_ability.configure(wraplength=self.winfo_width() - 25)
            items.configure(wraplength=self.winfo_width() - 25)
            title.configure(wraplength=self.winfo_width() - 25)
            abilities.configure(wraplength=self.winfo_width() - 25)
            proficiency.configure(wraplength=self.winfo_width() - 25)
            description.configure(wraplength=self.winfo_width() - 25)

        self.bind("<Configure>", reconfigure_labels)

    def create_buttons(self, show_search, show_home, show_edit, show_interface_verification):
        items_button = ttk.Button(
            self,
            text="Verify Items",
            command=lambda: show_interface_verification(self.items, 'Item', self.name, self.entity_type,
                                                        self.search_entities_name, self.search_type),
            state=button_state(self.items),
            cursor="hand2"
        )
        items_button.grid(column=0, sticky="EW")

        abilities_button = ttk.Button(
            self,
            text="Verify Abilities",
            command=lambda: show_interface_verification(self.abilities, 'Ability', self.name, self.entity_type,
                                                        self.search_entities_name, self.search_type),
            state=button_state(self.abilities),
            cursor="hand2"
        )
        abilities_button.grid(column=0, sticky="EW")

        titles_button = ttk.Button(
            self,
            text="Verify Titles",
            command=lambda: show_interface_verification(self.titles, 'Title', self.name, self.entity_type,
                                                        self.search_entities_name, self.search_type),
            state=button_state(self.titles),
            cursor="hand2"
        )
        titles_button.grid(column=0, sticky="EW")

        edit_button = ttk.Button(
            self,
            text="Edit",
            command=lambda: show_edit(self.entity, self.entity_type, self.name, self.entity_type,
                                      self.search_entities_name, self.search_type),
            cursor="hand2"
        )
        edit_button.grid(column=0, sticky="EW")

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
