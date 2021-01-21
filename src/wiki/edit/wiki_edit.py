import tkinter as tk
from tkinter import ttk, font

from src.wiki.wiki import Wiki


class WikiEdit(ttk.Frame):
    def __init__(self, container, wiki: Wiki):
        super().__init__(container)

        self.parent = container
        self.wiki = wiki

        self.wiki.update()

        self.categories = ['None'] + [category['name'] for category in self.wiki.categories]
        self.sections = ['None'] + [section['name'] for section in self.wiki.sections]
        self.chapters = ['None'] + [chapter['name'] for chapter in self.wiki.chapters]
        self.topics = ['None'] + [topic['name'] for topic in self.wiki.topics]

        # --- Variables ---
        self.category = tk.StringVar(value=self.categories[0])
        self.section = tk.StringVar(value=self.sections[0])
        self.chapter = tk.StringVar(value=self.chapters[0])
        self.topic = tk.StringVar(value=self.topics[0])

        self.create_widgets()

        self.create_buttons()

    def create_widgets(self):
        title = ttk.Label(
            self,
            text='Wiki Edition',
            font=font.Font(size=13)
        )
        title.grid(row=0, column=0, sticky='EW')

        title_separator = ttk.Separator(self)
        title_separator.grid(row=1, column=0, columnspan=1, sticky='EW')

        category_list = ttk.Combobox(
            self,
            textvariable=self.category,
            values=self.categories,
            state="readonly"
        )
        category_list.grid(row=2, column=0, sticky='EW')

        section_list = ttk.Combobox(
            self,
            textvariable=self.section,
            values=self.sections,
            state="readonly"
        )
        section_list.grid(row=3, column=0, sticky='EW')

        chapter_list = ttk.Combobox(
            self,
            textvariable=self.chapter,
            values=self.chapters,
            state="readonly"
        )
        chapter_list.grid(row=4, column=0, sticky='EW')

        topic_list = ttk.Combobox(
            self,
            textvariable=self.topic,
            values=self.topics,
            state="readonly"
        )
        topic_list.grid(row=5, column=0, sticky='EW')

    def create_buttons(self):
        wiki_separator = ttk.Separator(self)
        wiki_separator.grid(row=6, column=0, columnspan=1, sticky="EW")

        edit_category_button = ttk.Button(
            self,
            text='Edit Category',
            command=lambda: self.parent.create_frame('create_category'),
            cursor='hand2'
        )
        edit_category_button.grid(row=7, column=0, sticky="EW")

        edit_section_button = ttk.Button(
            self,
            text='Edit Section',
            command=lambda: self.parent.create_frame('create_category'),
            cursor='hand2'
        )
        edit_section_button.grid(row=8, column=0, sticky="EW")

        edit_chapter_button = ttk.Button(
            self,
            text='Edit Chapter',
            command=lambda: self.parent.create_frame('create_category'),
            cursor='hand2'
        )
        edit_chapter_button.grid(row=9, column=0, sticky="EW")

        edit_topic_button = ttk.Button(
            self,
            text='Edit Topic',
            command=lambda: self.parent.create_frame('create_category'),
            cursor='hand2'
        )
        edit_topic_button.grid(row=10, column=0, sticky="EW")

        back_button = ttk.Button(
            self,
            text='← Back',
            command=lambda: self.parent.create_frame('home'),
            cursor='hand2'
        )
        back_button.grid(row=11, column=0, sticky='EW')

    def select_section(self, section):
        self.parent.create_frame('section', section)
