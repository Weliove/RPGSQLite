import tkinter as tk
from tkinter import ttk

from src.connection.handle_items import get_item_abilities
from src.interface.interface_functions import generate_abilities, button_state
from src.item.item import Item


class ItemInterface(ttk.Frame):
    def __init__(self, container, entity, type_, show_search, show_home):
        super().__init__(container)

        print(entity)

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
        print(self.abilities)

        self.item = Item(self.name, self.name, self.type, self.reduction, self.damage, self.range, self.health,
                         self.area, self.abilities, self.effects, self.description)

        self.create_widgets()

        self.create_buttons(show_search, show_home)

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

    def create_buttons(self, show_search, show_home):
        abilities_button = ttk.Button(
            self,
            text="Verify Abilities",
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
