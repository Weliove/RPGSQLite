import tkinter as tk
from tkinter import ttk

from src.connection.database import search_database
from src.interface.item_interface import ItemInterface
from src.interface.user_interface import UserInterface


class InterfaceWidget(ttk.Frame):
    def __init__(self, container, entity, type_, show_search, show_home):
        super().__init__(container)

        self.entity = entity
        self.type_ = type_

        entity_type = search_database[type_]

        interface_widget_frame = None

        if entity_type == 'users':
            interface_widget_frame = UserInterface(self, entity, type_, show_search, show_home)
        elif entity_type == 'items':
            interface_widget_frame = ItemInterface(self, entity, type_, show_search, show_home)

        interface_widget_frame.grid(row=0, column=0, sticky="NSEW")
        interface_widget_frame.columnconfigure(0, weight=1)

        for child in interface_widget_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)
