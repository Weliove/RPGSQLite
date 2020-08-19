from tkinter import ttk

from src.connection.database import search_database
from src.interface.ability_interface import AbilityInterface
from src.interface.item_interface import ItemInterface
from src.interface.user_interface import UserInterface


class InterfaceVerificationWidget(ttk.Frame):
    def __init__(self, container, entities, type_, show_entity, show_home, show_interface_verification):
        super().__init__(container)

        self.entities = entities
        self.type_ = type_
        self.show_entity = show_entity
        self.show_home = show_home
        self.show_interface_verification = show_interface_verification

        self.frame_number = 0

        self.entity_type = search_database[type_]

        self.interface_widget_frames = []

        self.add_frame()

    def add_frame(self):
        for entity in self.entities:
            current_rows = self.grid_size()[1]

            if self.entity_type == 'items':
                new_frame = ItemInterface(self, entity, self.type_, self.show_entity, self.show_home,
                                          self.show_interface_verification)
            else:
                new_frame = AbilityInterface(self, entity, self.type_, self.show_entity, self.show_home,
                                             self.show_interface_verification)

            new_frame.grid(row=current_rows, column=0, sticky="NSEW")
            new_frame.columnconfigure(0, weight=1)

            for child in new_frame.winfo_children():
                child.grid_configure(padx=5, pady=5)

            self.interface_widget_frames.append(new_frame)
