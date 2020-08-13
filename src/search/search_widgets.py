import tkinter as tk
from tkinter import ttk


class SearchWidget(ttk.Frame):
    def __init__(self, parent, container, entities_name, type_, show_home):
        super().__init__(container)

        self.parent = parent
        self.container = container
        self.entities_name = entities_name
        self.show_home = show_home

        # --- Frame ---
        search_widget_frame = ttk.Frame(self)
        search_widget_frame.grid(row=0, column=0, sticky="NSEW")
        search_widget_frame.columnconfigure(0, weight=1)

        self.create_widgets(search_widget_frame, entities_name, type_)

        for child in search_widget_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def create_widgets(self, container, entities_name, type_):
        # --- Title ---

        result_entity_type = ttk.Label(
            container,
            text=type_ + 's'
        )
        result_entity_type.grid(column=0, padx=5, pady=5, sticky="EW")

        result_separator = ttk.Separator(
            container
        )
        result_separator.grid(column=0, columnspan=1, sticky="EW")

        for entity in entities_name:
            entity_button = ttk.Button(
                container,
                text=entity,
                command=lambda current_entity=entity: self.parent.search_result(current_entity),
                cursor="hand2"
            )
            entity_button.grid(column=0, padx=5, pady=5, sticky="EW")

        back_button = ttk.Button(
            container,
            text="← Back",
            command=self.show_home,
            cursor="hand2"
        )
        back_button.grid(column=0, padx=5, pady=5, sticky="EW")
