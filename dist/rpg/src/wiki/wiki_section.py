import tkinter as tk
from tkinter import ttk

from src.connection.handle_wiki import get_chapters_by_section_id


class WikiSection(ttk.Frame):
    def __init__(self, container, section, show_home):
        super().__init__(container)

        self.parent = container

        print(section)

        section_id = section['id']
        self.chapters = get_chapters_by_section_id(section_id)

        print(self.chapters)

        self.create_widgets(section, self.chapters)

        self.create_buttons()

    def create_widgets(self, section, chapters):
        section_name = section['name']

        title = ttk.Label(
            self,
            text=section_name
        )
        title.grid(column=0, sticky="EW")

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
            # command=lambda current_chapter=chapter: self.select_chapter(current_chapter),
            cursor='hand2'
        )
        chapter_button.grid(column=0, sticky="EW")

    def select_chapter(self, chapter):
        self.parent.create_frame('chapter', chapter)
