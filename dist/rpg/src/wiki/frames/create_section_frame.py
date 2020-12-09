import tkinter as tk
from tkinter import ttk

from src.wiki.wiki import Wiki


class CreateSectionFrame(ttk.Frame):
    def __init__(self, container, wiki: Wiki):
        super().__init__(container)

        self.wiki = wiki
        self.categories = [name['name'] for name in wiki.categories]

        self.name = tk.StringVar()
        self.category_name = tk.StringVar(value=self.categories[0])

        self.description_entry = tk.Text

        self.create_widgets()

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5, sticky='EW')

    def create_widgets(self):
        name_label = ttk.Label(
            self,
            text='Name'
        )
        name_label.grid(row=0, column=0)

        name_entry = ttk.Entry(
            self,
            textvariable=self.name,
            width=70
        )
        name_entry.grid(row=0, column=1)

        category_label = ttk.Label(
            self,
            text='Category'
        )
        category_label.grid(row=1, column=0)

        category_menu = ttk.Combobox(
            self,
            textvariable=self.category_name,
            values=self.categories,
            state="readonly"
        )
        category_menu.grid(row=1, column=1)

        description_label = ttk.Label(
            self,
            text='Description'
        )
        description_label.grid(row=2, column=0)

        self.description_entry = tk.Text(
            self,
            width=1,
            height=8
        )
        self.description_entry.grid(row=2, column=1)

    def get_category(self) -> dict:
        category_name = self.category_name.get()

        for category in self.wiki.categories:
            if category['name'] == category_name:
                return category

        return {}
