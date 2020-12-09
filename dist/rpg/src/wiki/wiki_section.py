import tkinter as tk
from tkinter import ttk, font

from src.wiki.wiki import Wiki


class WikiSection(ttk.Frame):
    def __init__(self, container, section, wiki: Wiki):
        super().__init__(container)

        self.parent = container
        self.wiki = wiki

        wiki.last_section = section

        print(section)

        section_id = section['id']
        self.chapters = self.wiki.get_chapters(section_id)

        print(self.chapters)

        self.create_widgets(section, self.chapters)

        self.create_buttons()

    def create_widgets(self, section, chapters):
        section_name = section['name']
        section_description = section['description']

        title = ttk.Label(
            self,
            text=section_name
        )
        title.grid(column=0, sticky="EW")

        if len(section_description) > 0:
            description = ttk.Label(
                self,
                text=section_description,
                font=font.Font(size=11)
            )
            description.grid(column=0, sticky='EW')

        title_separator = ttk.Separator(
            self
        )
        title_separator.grid(column=0, columnspan=1, sticky="EW")

        for chapter in chapters:
            chapter_name = chapter['name']

            chapter_button = ttk.Button(
                self,
                text=chapter_name,
                command=lambda current_chapter=chapter: self.select_chapter(current_chapter),
                cursor='hand2'
            )
            chapter_button.grid(column=0, sticky="EW")

    def create_buttons(self):
        wiki_separator = ttk.Separator(
            self
        )
        wiki_separator.grid(column=0, columnspan=1, sticky="EW")

        chapter_button = ttk.Button(
            self,
            text='Add Chapter',
            command=lambda: self.parent.create_frame('create_chapter'),
            cursor='hand2'
        )
        chapter_button.grid(column=0, sticky="EW")

        back_button = ttk.Button(
            self,
            text='← Back',
            command=lambda: self.parent.create_frame('home'),
            cursor='hand2'
        )
        back_button.grid(column=0, sticky='EW')

    def select_chapter(self, chapter):
        self.parent.create_frame('chapter', chapter)
