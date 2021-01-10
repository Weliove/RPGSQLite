import tkinter as tk
from tkinter import ttk, font

from src.ability.ability import Ability
from src.connection.handle_users import get_user_abilities
from src.edit.edit_functions import get_text_data, interface
from src.popup_info import popup_showinfo


class EditAbility(ttk.Frame):
    def __init__(self, container, entity, search_entities_name, search_type, show_interface,
                 show_interface_verification=None, interface_verification_dict=None):
        super().__init__(container)

        self.font = font.Font(size=11)
        self.search_entities_name = search_entities_name
        self.search_type = search_type
        self.show_interface = show_interface
        self.show_interface_verification = show_interface_verification
        self.interface_verification_dict = interface_verification_dict

        # --- Ability ---
        self.id = entity['id']
        self.ability_name = entity['name']
        self.ability_casting = entity['casting']
        self.ability_components = entity['components']
        self.ability_requirements = entity['requirements']
        self.ability_conditions = entity['conditions']
        self.ability_effects = entity['effects']
        self.ability_description = entity['description']

        # --- Attributes ---
        self.name = tk.StringVar(value=self.ability_name)
        self.casting = tk.StringVar(value=self.ability_casting)
        self.components = tk.StringVar(value=self.ability_components)

        # --- Widgets ---
        self.requirements_entry = tk.Text()
        self.conditions_entry = tk.Text()
        self.effects_entry = tk.Text()
        self.description_entry = tk.Text()

        self.create_widgets()

    def create_widgets(self):
        # --- Name ---

        name_label = ttk.Label(
            self,
            text="Name"
        )
        name_label.grid(row=0, column=0, sticky="EW")

        name_entry = ttk.Entry(
            self,
            textvariable=self.name,
            width=60
        )
        name_entry.grid(row=0, column=1, sticky="EW")

        # --- Casting ---

        casting_label = ttk.Label(
            self,
            text="Casting"
        )
        casting_label.grid(row=1, column=0, sticky="EW")

        casting_entry = ttk.Entry(
            self,
            textvariable=self.casting,
            width=60
        )
        casting_entry.grid(row=1, column=1, sticky="EW")

        # --- Components ---

        components_label = ttk.Label(
            self,
            text="Components"
        )
        components_label.grid(row=2, column=0, sticky="EW")

        components_entry = ttk.Entry(
            self,
            textvariable=self.components,
            width=60
        )
        components_entry.grid(row=2, column=1, sticky="EW")

        # --- Requirements ---

        requirements_label = ttk.Label(
            self,
            text="Requirements"
        )
        requirements_label.grid(row=3, column=0, sticky="EW")

        self.requirements_entry = tk.Text(
            self,
            width=1,
            height=3
        )
        self.requirements_entry.grid(row=3, column=1, sticky="EW")

        requirements_scroll = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.requirements_entry.yview
        )
        requirements_scroll.grid(row=3, column=2, sticky="ns")

        self.requirements_entry["yscrollcommand"] = requirements_scroll.set

        self.requirements_entry.insert(tk.END, self.ability_requirements)

        # --- Conditions ---

        conditions_label = ttk.Label(
            self,
            text="Conditions"
        )
        conditions_label.grid(row=4, column=0, sticky="EW")

        self.conditions_entry = tk.Text(
            self,
            width=1,
            height=3
        )
        self.conditions_entry.grid(row=4, column=1, sticky="EW")

        conditions_scroll = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.conditions_entry.yview
        )
        conditions_scroll.grid(row=4, column=2, sticky="ns")

        self.conditions_entry["yscrollcommand"] = conditions_scroll.set

        self.conditions_entry.insert(tk.END, self.ability_conditions)

        # --- Effects ---

        effects_label = ttk.Label(
            self,
            text="Effects"
        )
        effects_label.grid(row=5, column=0, sticky="EW")

        self.effects_entry = tk.Text(
            self,
            width=1,
            height=5
        )
        self.effects_entry.grid(row=5, column=1, sticky="EW")

        effects_scroll = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.effects_entry.yview
        )
        effects_scroll.grid(row=5, column=2, sticky="ns")

        self.effects_entry["yscrollcommand"] = effects_scroll.set

        self.effects_entry.insert(tk.END, self.ability_effects)

        # --- Description ---

        description_label = ttk.Label(
            self,
            text="Description"
        )
        description_label.grid(row=6, column=0, sticky="EW")

        self.description_entry = tk.Text(
            self,
            width=1,
            height=5
        )
        self.description_entry.grid(row=6, column=1, sticky="EW")

        description_scroll = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.description_entry.yview
        )
        description_scroll.grid(row=6, column=2, sticky="ns")

        self.description_entry["yscrollcommand"] = description_scroll.set

        self.description_entry.insert(tk.END, self.ability_description)

    def edit_entity(self):
        name = self.name.get()
        casting = self.casting.get()
        components = self.components.get()
        requirements = get_text_data(self.requirements_entry)
        conditions = get_text_data(self.conditions_entry)
        effects = get_text_data(self.effects_entry)
        description = get_text_data(self.description_entry)

        ability = Ability(name, casting, components, requirements, conditions, effects, description)

        update_ability = ability.update_ability(self.id)

        if not update_ability:
            if self.show_interface_verification is None:
                interface(name, 'Ability', self.show_interface, self.search_entities_name, self.search_type)
            else:
                user_name = self.interface_verification_dict['name']
                user_type = self.interface_verification_dict['type']
                abilities = get_user_abilities(user_name)

                self.show_interface_verification(abilities, 'Ability', user_name, user_type, self.search_entities_name,
                                                 self.search_type)
        else:
            popup_showinfo(update_ability)
