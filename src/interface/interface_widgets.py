from tkinter import ttk

from src.connection.database import search_database
from src.interface.ability_interface import AbilityInterface
from src.interface.item_interface import ItemInterface
from src.interface.title_interface import TitleInterface
from src.interface.user_interface import UserInterface


class InterfaceWidget(ttk.Frame):
    def __init__(self, container, entity, type_, show_search, show_home, show_edit, show_interface_verification,
                 search_entities_name, search_type):
        super().__init__(container)

        self.entity = entity
        self.type_ = type_

        entity_type = search_database[type_]

        interface_widget_frame = None

        if entity_type == 'users':
            interface_widget_frame = UserInterface(self, entity, type_, show_search, show_home, show_edit,
                                                   show_interface_verification, search_entities_name, search_type)
        elif entity_type == 'items':
            interface_widget_frame = ItemInterface(self, entity, type_, show_search, show_home, show_edit,
                                                   show_interface_verification)
        elif entity_type == 'abilities':
            interface_widget_frame = AbilityInterface(self, entity, type_, show_search, show_home, show_edit,
                                                      show_interface_verification)
        elif entity_type == 'titles':
            interface_widget_frame = TitleInterface(self, entity, type_, show_search, show_home, show_edit)

        interface_widget_frame.grid(row=0, column=0, sticky="NSEW")
        interface_widget_frame.columnconfigure(0, weight=1)

        for child in interface_widget_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)
