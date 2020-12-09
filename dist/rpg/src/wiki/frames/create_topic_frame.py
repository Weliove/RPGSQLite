import tkinter as tk
from tkinter import ttk

from src.wiki.wiki import Wiki


class CreateTopicFrame(ttk.Frame):
    def __init__(self, container, chapter, wiki: Wiki):
        super().__init__(container)

        self.wiki = wiki

        print(chapter)

        if chapter is None or chapter == 0:
            wiki_chapters = wiki.get_chapters()
            self.chapters = [name['name'] for name in wiki_chapters]
            self.chapter_name = tk.StringVar(value=self.chapters[0])
        else:
            self.chapters = chapter['name']
            self.chapter_name = tk.StringVar(value=self.chapters)

        self.name = tk.StringVar()

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

        chapter_label = ttk.Label(
            self,
            text='Chapter'
        )
        chapter_label.grid(row=1, column=0)

        chapter_menu = ttk.Combobox(
            self,
            textvariable=self.chapter_name,
            values=self.chapters,
            state="readonly"
        )
        chapter_menu.grid(row=1, column=1)

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

    def get_chapter(self) -> dict:
        chapter_name = self.chapter_name.get()

        for chapter in self.wiki.chapters:
            if chapter['name'] == chapter_name:
                return chapter

        return {}
