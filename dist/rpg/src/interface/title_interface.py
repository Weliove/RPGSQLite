from tkinter import ttk

from src.interface.interface_functions import interface
from src.title.title import Title


class TitleInterface(ttk.Frame):
    def __init__(self, container, entity, type_, show_search, show_home, show_edit, show_interface_verification,
                 parent_name=None, parent_type=None, ver=False, search_entities_name=None, search_type=None,
                 interface_verification_dict=None):
        super().__init__(container)

        self.entity = entity
        self.entity_type = type_

        self.show_interface_verification = show_interface_verification
        self.parent_name = parent_name
        self.parent_type = parent_type
        self.ver = ver
        self.search_entities_name = search_entities_name
        self.search_type = search_type
        self.interface_verification_dict = interface_verification_dict

        self.id = entity['id']
        self.name = entity['name']
        self.requirements = entity['requirements']
        self.description = entity['description']

        self.title = Title(self.name, self.requirements, self.description)

        self.create_widgets()

        self.create_buttons(show_search, show_home, show_edit)

    def create_widgets(self):
        # --- Title ---

        name = ttk.Label(
            self,
            text=self.name
        )
        name.grid(row=0, column=0, sticky="EW")

        name_separator = ttk.Separator(
            self
        )
        name_separator.grid(row=1, column=0, columnspan=1, sticky="EW")

        # --- Requirements ---

        requirements = ttk.Label(
            self,
            text=f'Requirements:  {self.requirements}'
        )
        requirements.grid(row=2, column=0, sticky="EW")

        # --- Description ---

        description = ttk.Label(
            self,
            text=f'Description:  {self.description}'
        )
        description.grid(row=3, column=0, sticky="EW")

        def reconfigure_labels(event):
            requirements.configure(wraplength=self.winfo_width() - 25)
            description.configure(wraplength=self.winfo_width() - 25)

        self.bind("<Configure>", reconfigure_labels)

    def create_buttons(self, show_search, show_home, show_edit):
        edit_button = ttk.Button(
            self,
            text="Edit",
            command=lambda: show_edit(self.entity, self.entity_type, self.parent_name, self.parent_type,
                                      self.search_entities_name, self.search_type, self.show_interface_verification,
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
