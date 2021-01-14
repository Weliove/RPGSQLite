import tkinter as tk
from tkinter import ttk, font

from src.connection.handle_users import get_user_titles
from src.edit.edit_functions import get_text_data, interface
from src.popup_info import popup_showinfo
from src.title.title import Title


class EditTitle(ttk.Frame):
    def __init__(self, container, entity, search_entities_name, search_type, show_interface,
                 show_interface_verification=None, interface_verification_dict=None):
        super().__init__(container)

        self.font = font.Font(size=11)
        self.search_entities_name = search_entities_name
        self.search_type = search_type
        self.show_interface = show_interface
        self.show_interface_verification = show_interface_verification
        self.interface_verification_dict = interface_verification_dict

        # --- Title ---
        self.id = entity['id']
        self.title_name = entity['name']
        self.title_requirements = entity['requirements']
        self.title_description = entity['description']

        # --- Attributes ---
        self.name = tk.StringVar(value=self.title_name)

        # --- Widgets ---
        self.requirements_entry = tk.Text()
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

        # --- Requirements ---

        requirements_label = ttk.Label(
            self,
            text="Requirements"
        )
        requirements_label.grid(row=1, column=0, sticky="EW")

        self.requirements_entry = tk.Text(
            self,
            width=1,
            height=5
        )
        self.requirements_entry.grid(row=1, column=1, sticky="EW")

        requirements_scroll = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.requirements_entry.yview
        )
        requirements_scroll.grid(row=1, column=2, sticky="ns")

        self.requirements_entry["yscrollcommand"] = requirements_scroll.set

        self.requirements_entry.insert(tk.END, self.title_requirements)

        # --- Description ---

        description_label = ttk.Label(
            self,
            text="Description"
        )
        description_label.grid(row=2, column=0, sticky="EW")

        self.description_entry = tk.Text(
            self,
            width=1,
            height=5
        )
        self.description_entry.grid(row=2, column=1, sticky="EW")

        description_scroll = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.description_entry.yview
        )
        description_scroll.grid(row=2, column=2, sticky="ns")

        self.description_entry["yscrollcommand"] = description_scroll.set

        self.description_entry.insert(tk.END, self.title_description)

    def edit_entity(self):
        name = self.name.get()
        requirements = get_text_data(self.requirements_entry)
        description = get_text_data(self.description_entry)

        title = Title(name, requirements, description)

        edit_title = title.update_title(self.id)

        if not edit_title:
            if self.show_interface_verification is None or self.interface_verification_dict is None:
                interface(name, 'Title', self.show_interface, self.search_entities_name, self.search_type)
            else:
                user_name = self.interface_verification_dict['name']
                user_type = self.interface_verification_dict['type']
                titles = get_user_titles(user_name)

                self.show_interface_verification(titles, 'Title', user_name, user_type, self.search_entities_name,
                                                 self.search_type)
        else:
            popup_showinfo(edit_title)
