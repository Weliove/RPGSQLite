import tkinter as tk
from tkinter import ttk, font

from src.connection.handle_users import get_user_proficiencies
from src.edit.edit_functions import get_text_data, interface
from src.popup_info import popup_showinfo
from src.proficiency.proficiency import Proficiency


class EditProficiency(ttk.Frame):
    def __init__(self, container, entity, search_entities_name, search_type, show_interface,
                 show_interface_verification=None, interface_verification_dict=None):
        super().__init__(container)

        self.font = font.Font(size=11)
        self.search_entities_name = search_entities_name
        self.search_type = search_type
        self.show_interface = show_interface
        self.show_interface_verification = show_interface_verification
        self.interface_verification_dict = interface_verification_dict

        # --- Proficiency ---
        self.id = entity['id']
        self.proficiency_name = entity['name']
        self.proficiency_description = entity['description']

        # --- Attributes ---
        self.name = tk.StringVar(value=self.proficiency_name)

        # --- Widgets ---
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

        # --- Description ---
        description_label = ttk.Label(
            self,
            text="Description"
        )
        description_label.grid(row=3, column=0, sticky="EW")

        self.description_entry = tk.Text(
            self,
            width=1,
            height=5
        )
        self.description_entry.grid(row=3, column=1, sticky="EW")

        description_scroll = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.description_entry.yview
        )
        description_scroll.grid(row=3, column=2, sticky="ns")

        self.description_entry["yscrollcommand"] = description_scroll.set

        self.description_entry.insert(tk.END, self.proficiency_description)

    def edit_entity(self):
        name = self.name.get()
        description = get_text_data(self.description_entry)

        data = 'Proficiency'

        proficiency = Proficiency(name, description)

        edit_proficiency = proficiency.update_proficiency(self.id)

        if not edit_proficiency:
            if self.show_interface_verification is None or self.interface_verification_dict is None:
                interface(name, data, self.show_interface, self.search_entities_name, self.search_type)
            else:
                user_name = self.interface_verification_dict['name']
                user_type = self.interface_verification_dict['type']
                proficiencies = get_user_proficiencies(user_name)

                self.show_interface_verification(proficiencies, data, user_name, user_type,
                                                 self.search_entities_name, self.search_type)
        else:
            popup_showinfo(edit_proficiency)
