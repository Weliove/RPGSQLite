import tkinter as tk
from tkinter import ttk

from src.wiki.wiki import Wiki


class CreateChapterFrame(ttk.Frame):
    def __init__(self, container, wiki: Wiki):
        super().__init__(container)

        self.wiki = wiki

        if len(wiki.sections) == 0:
            wiki.get_sections()

        self.sections = [name['name'] for name in wiki.sections]

        self.name = tk.StringVar()
        self.section_name = tk.StringVar(value=self.sections[0])

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

        section_label = ttk.Label(
            self,
            text='Section'
        )
        section_label.grid(row=1, column=0)

        section_menu = ttk.Combobox(
            self,
            textvariable=self.section_name,
            values=self.sections,
            state="readonly"
        )
        section_menu.grid(row=1, column=1)

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

    def get_section(self) -> dict:
        section_name = self.section_name.get()

        for section in self.wiki.sections:
            if section['name'] == section_name:
                return section

        return {}
