import tkinter as tk
from tkinter import ttk

from src.connection.database import get_search_entities
from src.home.home_widget import HomeWidget
from src.popup_info import popup_showinfo


class Home(ttk.Frame):
    def __init__(self, parent, create_avatar):
        super().__init__(parent)

        self.parent = parent
        self.create_avatar = create_avatar

        # --- Create Widget Frame ---

        self.home_widgets = HomeWidget(self)
        self.home_widgets.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

        # --- Create Button Frame ---

        home_buttons = ttk.Frame(self)
        home_buttons.grid(row=1, column=0, padx=10, pady=10, sticky="EW")
        home_buttons.columnconfigure(0, weight=1)

        self.create_buttons(home_buttons)

        for child in home_buttons.winfo_children():
            child.grid_configure(padx=15, pady=5)

    def create_buttons(self, container):
        search_button = ttk.Button(
            container,
            text="Search",
            command=self.search,
            cursor="hand2"
        )
        search_button.grid(row=0, column=0, sticky="EW")

        create_avatar_button = ttk.Button(
            container,
            text="Create Avatar",
            command=self.create_avatar,
            cursor="hand2"
        )
        create_avatar_button.grid(row=1, column=0, sticky="EW")

        create_item_button = ttk.Button(
            container,
            text="Create Item",
            cursor="hand2"
        )
        create_item_button.grid(row=2, column=0, sticky="EW")

        create_ability_button = ttk.Button(
            container,
            text="Create Ability",
            cursor="hand2"
        )
        create_ability_button.grid(row=3, column=0, sticky="EW")

        create_title_button = ttk.Button(
            container,
            text="Create Ability",
            cursor="hand2"
        )
        create_title_button.grid(row=4, column=0, sticky="EW")

        create_wiki_button = ttk.Button(
            container,
            text="Create Wiki",
            cursor="hand2"
        )
        create_wiki_button.grid(row=5, column=0, sticky="EW")

    def search(self):
        name = self.home_widgets.name.get()
        type_ = self.home_widgets.type_choice.get()

        search_result = get_search_entities(name, type_)

        if search_result:
            self.parent.show_search(search_result, type_)
            self.home_widgets.name.set('')
        else:
            popup_showinfo(f"{name} not found!")
