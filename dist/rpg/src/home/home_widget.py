import tkinter as tk
from tkinter import ttk


class HomeWidget(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        # --- Type values for search ---
        self.type_values = ("Character", "NPC", "Monster", "Armor", "Weapon", "Title", "Ability", "Wiki")

        # --- Attributes ---
        self.name = tk.StringVar()
        self.type_choice = tk.StringVar(value=self.type_values[0])

        # --- Frame ---
        home_widgets_frame = ttk.Frame(self)
        home_widgets_frame.grid(row=0, column=0, sticky="NSEW")
        home_widgets_frame.columnconfigure((0, 1), weight=1)

        self.create_widgets(home_widgets_frame)

        for child in home_widgets_frame.winfo_children():
            child.grid_configure(padx=15, pady=5)

    def create_widgets(self, container):
        name_label = ttk.Label(
            container,
            text="Name"
        )
        name_label.grid(row=0, column=0, sticky="EW")

        name_entry = ttk.Entry(
            container,
            textvariable=self.name,
            width=70
        )
        name_entry.grid(row=0, column=1, sticky="EW")

        # name_entry.bind("<Return>", self.search_entity)
        # name_entry.bind("<KP_Enter>", self.search_entity)

        type_label = ttk.Label(
            container,
            text="Type"
        )
        type_label.grid(row=1, column=0, sticky="EW")

        type_entry = ttk.Combobox(
            container,
            textvariable=self.type_choice,
            values=self.type_values,
            state="readonly"
        )
        type_entry.grid(row=1, column=1, sticky="EW")
