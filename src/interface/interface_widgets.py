import tkinter as tk
from tkinter import ttk

from src.connection.database import search_database
from src.interface.user_interface import UserInterface


class InterfaceWidget(ttk.Frame):
    def __init__(self, container, entity, type_, show_home):
        super().__init__(container)

        self.entity = entity
        self.type_ = type_

        # entity_type = search_database[type_]

        # if entity_type == 'users':
        interface_widget_frame = UserInterface(self, entity, type_, show_home)
        interface_widget_frame.grid(row=0, column=0, sticky="NSEW")
        interface_widget_frame.columnconfigure(0, weight=1)

        for child in interface_widget_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)
