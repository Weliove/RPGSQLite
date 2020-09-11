import tkinter as tk
from tkinter import ttk

from src.connection.handle_wiki import get_categories, get_sections, get_sections_by_category_id


class WikiHome(ttk.Frame):
    def __init__(self, container, show_home):
        super().__init__(container)

        self.parent = container

        categories = get_categories()

        self.set_widgets(categories)

        self.create_buttons()

    def create_widgets(self, category, sections):
        category_name = category['name']

        title = ttk.Label(
            self,
            text=category_name
        )
        title.grid(column=0, sticky="EW")

        title_separator = ttk.Separator(
            self
        )
        title_separator.grid(column=0, columnspan=1, sticky="EW")

        for section in sections:
            section_name = section['name']

            section_button = ttk.Button(
                self,
                text=section_name,
                command=lambda current_section=section: self.select_section(current_section),
                cursor='hand2'
            )
            section_button.grid(column=0, sticky="EW")

    def create_buttons(self):
        wiki_separator = ttk.Separator(
            self
        )
        wiki_separator.grid(column=0, columnspan=1, sticky="EW")

        create_category_button = ttk.Button(
            self,
            text='Create Category',
            cursor='hand2'
        )
        create_category_button.grid(column=0, sticky="EW")

        create_section_button = ttk.Button(
            self,
            text='Create Section',
            cursor='hand2'
        )
        create_section_button.grid(column=0, sticky="EW")

        create_chapter_button = ttk.Button(
            self,
            text='Create Chapter',
            cursor='hand2'
        )
        create_chapter_button.grid(column=0, sticky="EW")

    def select_section(self, section):
        self.parent.create_frame('section', section)

    def set_widgets(self, categories):
        for category in categories:
            category_id = category['id']
            sections = get_sections_by_category_id(category_id)

            self.create_widgets(category, sections)
