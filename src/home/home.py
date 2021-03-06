import tkinter as tk
from tkinter import ttk

from src.connection.database import get_search_entities
from src.home.home_widget import HomeWidget
from src.popup_info import popup_showinfo


class Home(ttk.Frame):
    def __init__(self, parent, create_avatar, create_item, create_ability, create_title, create_proficiency,
                 create_wiki):
        super().__init__(parent)

        self.parent = parent
        self.create_avatar = create_avatar
        self.create_item = create_item
        self.create_ability = create_ability
        self.create_title = create_title
        self.create_proficiency = create_proficiency
        self.create_wiki = create_wiki

        # --- Create Widget Frame ---

        self.home_widgets = HomeWidget(self)
        self.home_widgets.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

        # --- Create Button Frame ---

        home_buttons = ttk.Frame(self)
        home_buttons.grid(row=1, column=0, padx=10, pady=10, sticky="EW")
        home_buttons.columnconfigure(0, weight=1)

        self.create_buttons(home_buttons)

        for child in home_buttons.winfo_children():
            child.grid_configure(column=0, padx=15, pady=5, sticky='EW')

    def create_buttons(self, container):
        search_button = ttk.Button(
            container,
            text="Search",
            command=self.search,
            cursor="hand2"
        )
        search_button.grid(row=0)

        create_avatar_button = ttk.Button(
            container,
            text="Create Avatar",
            command=self.create_avatar,
            cursor="hand2"
        )
        create_avatar_button.grid(row=1)

        create_item_button = ttk.Button(
            container,
            text="Create Item",
            command=self.create_item,
            cursor="hand2"
        )
        create_item_button.grid(row=2)

        create_ability_button = ttk.Button(
            container,
            text="Create Ability",
            command=self.create_ability,
            cursor="hand2"
        )
        create_ability_button.grid(row=3)

        create_title_button = ttk.Button(
            container,
            text="Create Title",
            command=self.create_title,
            cursor="hand2"
        )
        create_title_button.grid(row=4)

        create_proficiency_button = ttk.Button(
            container,
            text='Create Proficiency',
            command=self.create_proficiency,
            cursor='hand2'
        )
        create_proficiency_button.grid(row=5)

        create_wiki_button = ttk.Button(
            container,
            text="Wiki",
            command=self.create_wiki,
            cursor="hand2"
        )
        create_wiki_button.grid(row=6)

    def search(self):
        name = self.home_widgets.name.get()
        type_ = self.home_widgets.type_choice.get()

        search_result = get_search_entities(name, type_)

        if search_result:
            self.parent.show_search(search_result, type_)
            self.home_widgets.name.set('')
        else:
            popup_showinfo(f"{name} not found!")
