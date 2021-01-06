import tkinter as tk
from tkinter import ttk

from src.connection.handle_items import get_item_abilities
from src.interface.interface_functions import generate_abilities, button_state, interface
from src.item.item import Item


class ItemInterface(ttk.Frame):
    def __init__(self, container, entity, type_, show_search, show_home, show_edit, show_interface_verification,
                 parent_name=None, parent_type=None, ver=False, search_entities_name=None, search_type=None):
        super().__init__(container)

        print(show_search)

        self.container = container

        self.parent_name = parent_name
        self.parent_type = parent_type
        self.ver = ver
        self.search_entities_name = search_entities_name
        self.search_type = search_type

        self.entity = entity
        self.entity_type = type_

        self.types_ = {1: 'Armor', 2: 'Weapon'}

        self.id = entity['id']
        self.name = entity['name']
        self.type = entity['type']
        self.reduction = entity['reduction']
        self.damage = entity['damage']
        self.range = entity['range']
        self.health = entity['health']
        self.area = entity['area']
        self.effects = entity['effects']
        self.description = entity['description']

        self.abilities = get_item_abilities(self.id)
        print(f'>>>> abilities: {self.abilities}')

        self.item = Item(self.name, self.name, self.type, self.reduction, self.damage, self.range, self.health,
                         self.area, self.abilities, self.effects, self.description)

        self.create_widgets()

        self.create_buttons(show_search, show_home, show_edit, show_interface_verification)

    def create_widgets(self):
        # --- Item ---

        name = ttk.Label(
            self,
            text=self.name
        )
        name.grid(row=0, column=0, sticky="EW")

        name_separator = ttk.Separator(
            self
        )
        name_separator.grid(row=1, column=0, columnspan=1, sticky="EW")

        # --- Type ---

        type_ = ttk.Label(
            self,
            text='Type:  ' + self.types_[self.type]
        )
        type_.grid(row=2, column=0, sticky="EW")

        # --- Reduction ---

        reduction = ttk.Label(
            self,
            text='Reduction:  ' + self.reduction
        )
        reduction.grid(row=3, column=0, sticky="EW")

        # --- Damage ---

        damage = ttk.Label(
            self,
            text='Damage:  ' + self.damage
        )
        damage.grid(row=4, column=0, sticky="EW")

        # --- Range ---

        range_ = ttk.Label(
            self,
            text='Range:  ' + self.range
        )
        range_.grid(row=5, column=0, sticky="EW")

        # --- Health ---

        health = ttk.Label(
            self,
            text='Health:  ' + self.health
        )
        health.grid(row=6, column=0, sticky="EW")

        # --- Area ---

        area = ttk.Label(
            self,
            text='Area:  ' + self.area
        )
        area.grid(row=7, column=0, sticky="EW")

        # --- Abilities ---

        abilities = ttk.Label(
            self,
            text=generate_abilities(self.abilities)
        )
        abilities.grid(row=8, column=0, sticky="EW")

        # --- Effects ---

        effects = ttk.Label(
            self,
            text='Effects:  ' + self.effects
        )
        effects.grid(row=9, column=0, sticky="EW")

        # --- Description ---

        description = ttk.Label(
            self,
            text='Description:  ' + self.description
        )
        description.grid(row=10, column=0, sticky="EW")

        def reconfigure_labels(event):
            abilities.configure(wraplength=self.winfo_width() - 25)
            effects.configure(wraplength=self.winfo_width() - 25)
            description.configure(wraplength=self.winfo_width() - 25)

        self.bind("<Configure>", reconfigure_labels)

    def create_buttons(self, show_search, show_home, show_edit, show_interface_verification):
        abilities_button = ttk.Button(
            self,
            text="Verify Abilities",
            command=lambda: show_interface_verification(self.abilities, 'Ability'),
            state=button_state(self.abilities),
            cursor="hand2"
        )
        abilities_button.grid(column=0, sticky="EW")

        print(self.parent_name)

        edit_button = ttk.Button(
            self,
            text="Edit",
            command=lambda: show_edit(self.entity, self.entity_type, self.parent_name, self.parent_type,
                                      self.search_entities_name, self.search_type),
            cursor="hand2"
        )
        edit_button.grid(column=0, sticky="EW")

        back_button = ttk.Button(
            self,
            text="← Back",
            command=lambda: self.back(show_search),
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

    def back(self, show_search):
        if self.ver:
            interface(self.parent_name, self.parent_type, show_search, self.search_entities_name, self.search_type)
        else:
            show_search()
