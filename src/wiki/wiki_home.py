import tkinter as tk
from tkinter import ttk, font

from src.wiki.wiki import Wiki


class WikiHome(ttk.Frame):
    def __init__(self, container, wiki: Wiki):
        super().__init__(container)

        self.parent = container
        self.wiki = wiki

        wiki.last_section = {}
        wiki.last_chapter = {}
        wiki.last_topic = {}

        categories = self.wiki.get_categories()

        self.set_widgets(categories)

        self.create_buttons()

    def create_widgets(self, category, sections):
        category_name = category['name']
        category_description = category['description']

        title = ttk.Label(
            self,
            text=category_name,
            font=font.Font(size=13)
        )
        title.grid(column=0, sticky='EW')

        if len(category_description) > 0:
            description = ttk.Label(
                self,
                text=category_description,
                font=font.Font(size=11)
            )
            description.grid(column=0, sticky='EW')

        title_separator = ttk.Separator(
            self
        )
        title_separator.grid(column=0, columnspan=1, sticky='EW')

        for section in sections:
            section_name = section['name']

            section_button = ttk.Button(
                self,
                text=section_name,
                command=lambda current_section=section: self.select_section(current_section),
                cursor='hand2'
            )
            section_button.grid(column=0, sticky='EW')

    def create_buttons(self):
        wiki_separator = ttk.Separator(
            self
        )
        wiki_separator.grid(column=0, columnspan=1, sticky="EW")

        create_category_button = ttk.Button(
            self,
            text='Create Category',
            command=lambda: self.parent.create_frame('create_category'),
            cursor='hand2'
        )
        create_category_button.grid(column=0, sticky="EW")

        create_section_button = ttk.Button(
            self,
            text='Create Section',
            command=lambda: self.parent.create_frame('create_section'),
            state=tk.DISABLED if len(self.wiki.categories) == 0 else tk.NORMAL,
            cursor='hand2'
        )
        create_section_button.grid(column=0, sticky="EW")

        create_chapter_button = ttk.Button(
            self,
            text='Create Chapter',
            command=lambda: self.parent.create_frame('create_chapter'),
            state=tk.DISABLED if len(self.wiki.get_sections()) == 0 else tk.NORMAL,
            cursor='hand2'
        )
        create_chapter_button.grid(column=0, sticky="EW")

        create_topic_button = ttk.Button(
            self,
            text='Create Topic',
            command=lambda: self.parent.create_frame('create_topic'),
            state=tk.DISABLED if len(self.wiki.get_chapters()) == 0 else tk.NORMAL,
            cursor='hand2'
        )
        create_topic_button.grid(column=0, sticky="EW")

    def select_section(self, section):
        self.parent.create_frame('section', section)

    def set_widgets(self, categories):
        if len(categories) == 0:
            return

        for category in categories:
            category_id = category['id']
            sections = self.wiki.get_sections(category_id)

            self.create_widgets(category, sections)
