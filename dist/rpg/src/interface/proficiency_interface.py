import tkinter as tk
from tkinter import ttk

from src.edit.edit_functions import interface


class ProficiencyInterface(ttk.Frame):
    def __init__(self, container, entity, type_, show_search, show_home, show_edit, show_interface_verification=None,
                 parent_name=None, parent_type=None, ver=False, search_entities_name=None, search_type=None,
                 interface_verification_dict=None):
        super().__init__(container)

        self.container = container

        self.parent_name = parent_name
        self.parent_type = parent_type
        self.ver = ver
        self.search_entities_name = search_entities_name
        self.search_type = search_type
        self.interface_verification_dict = interface_verification_dict

        self.entity = entity
        self.entity_type = type_

        self.id = entity['id']
        self.name = entity['name']
        self.description = entity['description']

        self.create_widgets()

        self.create_buttons(show_search, show_home, show_edit, show_interface_verification)

    def create_widgets(self):
        # --- Proficiency ---

        name = ttk.Label(
            self,
            text=self.name
        )
        name.grid(row=0, column=0, sticky="EW")

        name_separator = ttk.Separator(
            self
        )
        name_separator.grid(row=1, column=0, columnspan=1, sticky="EW")

        # --- Description ---

        description = ttk.Label(
            self,
            text='Description:  ' + self.description
        )
        description.grid(row=10, column=0, sticky="EW")

        def reconfigure_labels(event):
            description.configure(wraplength=self.winfo_width() - 25)

        self.bind("<Configure>", reconfigure_labels)

    def create_buttons(self, show_search, show_home, show_edit, show_interface_verification):
        edit_button = ttk.Button(
            self,
            text="Edit",
            command=lambda: show_edit(self.entity, self.entity_type, self.parent_name, self.parent_type,
                                      self.search_entities_name, self.search_type, show_interface_verification,
                                      self.interface_verification_dict),
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
