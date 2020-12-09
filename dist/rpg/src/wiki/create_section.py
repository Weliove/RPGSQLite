import tkinter as tk
from tkinter import ttk

from src.popup_info import popup_showinfo
from src.wiki.frames.create_section_frame import CreateSectionFrame
from src.wiki.wiki import Wiki


class CreateSection(ttk.Frame):
    def __init__(self, container, wiki: Wiki):
        super().__init__(container)

        self.parent = container
        self.wiki = wiki

        self.widgets_frame = CreateSectionFrame(self, wiki)
        self.widgets_frame.grid(row=0, column=0, sticky='NSEW')
        self.widgets_frame.columnconfigure(0, weight=1)

        buttons_frame = ttk.Frame(self)
        buttons_frame.grid(row=1, column=0, sticky='EW')
        buttons_frame.columnconfigure(0, weight=1)

        self.create_buttons(buttons_frame)

        for child in buttons_frame.winfo_children():
            child.grid_configure(padx=5, pady=5, sticky='EW')

    def create_buttons(self, container):
        wiki_separator = ttk.Separator(
            container
        )
        wiki_separator.grid(row=0, column=0, columnspan=1, sticky="EW")

        create_button = ttk.Button(
            container,
            text='Create',
            command=self.create_section,
            cursor='hand2'
        )
        create_button.grid(row=1, column=0, sticky="EW")

        back_button = ttk.Button(
            container,
            text='← Back',
            command=lambda: self.parent.create_frame('home'),
            cursor='hand2'
        )
        back_button.grid(row=2, column=0, sticky='EW')

    def create_section(self):
        name = self.widgets_frame.name.get()
        description = self.get_text_data(self.widgets_frame.description_entry)
        category = self.widgets_frame.get_category()
        category_id = category['id']

        create = self.wiki.create_section(name, description, category_id)

        self.parent.create_frame('home') if create else popup_showinfo('Error!')

    def get_text_data(self, text_widget):
        return text_widget.get("1.0", 'end-1c')
