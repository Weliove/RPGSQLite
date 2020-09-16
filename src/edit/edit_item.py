import tkinter as tk
from tkinter import ttk, font

from src.connection.database import get_entity
from src.connection.handle_abilities import get_abilities_name_by_type
from src.connection.handle_items import get_item_abilities
from src.edit.edit_functions import get_text_data, set_stored_items, handle_selection_change
from src.item.item import Item
from src.item.item_properties import get_entity_ids
from src.popup_info import popup_showinfo


class EditItem(ttk.Frame):
    def __init__(self, container, entity, show_interface):
        super().__init__(container)

        self.font = font.Font(size=11)
        self.show_interface = show_interface

        self.types_ = ('Armor', 'Weapon')

        # --- Item ---
        self.id = entity['id']
        self.item_name = entity['name']
        self.item_type = entity['type']
        self.item_reduction = entity['reduction']
        self.item_damage = entity['damage']
        self.item_range = entity['range']
        self.item_health = entity['health']
        self.item_area = entity['area']
        self.item_effects = entity['effects']
        self.item_description = entity['description']

        self.abilities = ['None'] + get_abilities_name_by_type(4)
        self.item_abilities = get_item_abilities(self.id)

        # --- Attributes ---
        self.name = tk.StringVar(value=self.item_name)
        self.type_ = tk.StringVar(value=self.types_[self.item_type - 1])
        self.reduction = tk.StringVar(value=self.item_reduction)
        self.damage = tk.StringVar(value=self.item_damage)
        self.range_ = tk.StringVar(value=self.item_range)
        self.health = tk.StringVar(value=self.item_health)
        self.area = tk.StringVar(value=self.item_area)

        self.ability = tk.StringVar(value=self.abilities)

        # --- Widgets ---
        self.abilities_entry = tk.Listbox()
        self.effects_entry = tk.Text()
        self.description_entry = tk.Text()

        self.create_widgets()

    def create_widgets(self):
        # --- Name ---

        name_label = ttk.Label(
            self,
            text="Name"
        )
        name_label.grid(row=2, column=0, sticky="EW")

        name_entry = ttk.Entry(
            self,
            textvariable=self.name,
            width=60
        )
        name_entry.grid(row=2, column=1, sticky="EW")

        # --- Type ---

        type_label = ttk.Label(
            self,
            text="Type"
        )
        type_label.grid(row=6, column=0, sticky="EW")

        type_entry = ttk.Combobox(
            self,
            textvariable=self.type_,
            values=self.types_,
            exportselection=False,
            state="readonly"
        )
        type_entry.grid(row=6, column=1, sticky="EW")

        # --- Reduction ---

        reduction_label = ttk.Label(
            self,
            text="Reduction"
        )
        reduction_label.grid(row=7, column=0, sticky="EW")

        reduction_entry = ttk.Entry(
            self,
            textvariable=self.reduction,
            width=60
        )
        reduction_entry.grid(row=7, column=1, sticky="EW")

        # --- Damage ---

        damage_label = ttk.Label(
            self,
            text="Damage"
        )
        damage_label.grid(row=8, column=0, sticky="EW")

        damage_entry = ttk.Entry(
            self,
            textvariable=self.damage,
            width=60
        )
        damage_entry.grid(row=8, column=1, sticky="EW")

        # --- Range ---

        range_label = ttk.Label(
            self,
            text="Range"
        )
        range_label.grid(row=9, column=0, sticky="EW")

        range_entry = ttk.Entry(
            self,
            textvariable=self.range_,
            width=60
        )
        range_entry.grid(row=9, column=1, sticky="EW")

        # --- Health ---

        health_label = ttk.Label(
            self,
            text="Health"
        )
        health_label.grid(row=10, column=0, sticky="EW")

        health_entry = ttk.Entry(
            self,
            textvariable=self.health,
            width=60
        )
        health_entry.grid(row=10, column=1, sticky="EW")

        # --- Area ---

        area_label = ttk.Label(
            self,
            text="Area"
        )
        area_label.grid(row=11, column=0, sticky="EW")

        area_entry = ttk.Entry(
            self,
            textvariable=self.area,
            width=60
        )
        area_entry.grid(row=11, column=1, sticky="EW")

        # --- Abilities ---

        abilities_label = ttk.Label(
            self,
            text="Abilities"
        )
        abilities_label.grid(row=12, column=0, sticky="EW")

        self.abilities_entry = tk.Listbox(
            self,
            listvariable=self.ability,
            selectmode="extended",
            exportselection=False,
            selectbackground="#2CCC5B",
            highlightcolor="#1DE557",
            font=self.font,
            width=1,
            height=5
        )
        self.abilities_entry.grid(row=12, column=1, sticky="EW")

        set_stored_items(self.abilities_entry, self.item_abilities, self.abilities)

        # self.abilities_entry.select_set(0)

        abilities_scrollbar = ttk.Scrollbar(self, orient="vertical")
        abilities_scrollbar.config(command=self.abilities_entry.yview)
        abilities_scrollbar.grid(row=12, column=2, sticky="NS")

        self.abilities_entry.config(yscrollcommand=abilities_scrollbar.set)

        # --- Effects ---

        effects_label = ttk.Label(
            self,
            text="Effects"
        )
        effects_label.grid(row=13, column=0, sticky="EW")

        self.effects_entry = tk.Text(
            self,
            width=1,
            height=5
        )
        self.effects_entry.grid(row=13, column=1, sticky="EW")

        effects_scroll = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.effects_entry.yview
        )
        effects_scroll.grid(row=13, column=2, sticky="ns")

        self.effects_entry["yscrollcommand"] = effects_scroll.set

        self.effects_entry.insert(tk.END, self.item_effects)

        # --- Description ---

        description_label = ttk.Label(
            self,
            text="Description"
        )
        description_label.grid(row=14, column=0, sticky="EW")

        self.description_entry = tk.Text(
            self,
            width=1,
            height=5
        )
        self.description_entry.grid(row=14, column=1, sticky="EW")

        description_scroll = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.description_entry.yview
        )
        description_scroll.grid(row=14, column=2, sticky="ns")

        self.description_entry["yscrollcommand"] = description_scroll.set

        self.description_entry.insert(tk.END, self.item_description)

    def edit_entity(self):
        type_dict = {'Armor': 1, 'Weapon': 2}

        abilities = handle_selection_change(self.abilities_entry, self.abilities)
        abilities_result = get_entity_ids('ability', abilities)

        name = self.name.get()
        type_ = type_dict[self.type_.get()]
        reduction = self.reduction.get()
        damage = self.damage.get()
        range_ = self.range_.get()
        health = self.health.get()
        area = self.area.get()
        effects = get_text_data(self.effects_entry)
        description = get_text_data(self.description_entry)

        item = Item(name, type_, reduction, damage, range_, health, area, abilities_result, effects,
                    description)

        update_item = item.update_item(self.id)

        self.interface(name, self.type_.get()) if not update_item else popup_showinfo(update_item)

    def interface(self, name, type_):
        new_item = get_entity(name, type_)
        self.show_interface(new_item, type_)
