from tkinter import ttk
from typing import Union

from src.wiki.create_category import CreateCategory
from src.wiki.wiki import Wiki
from src.wiki.wiki_chapter import WikiChapter
from src.wiki.wiki_home import WikiHome
from src.wiki.wiki_section import WikiSection


class WikiWidget(ttk.Frame):
    def __init__(self, container, session, show_home):
        super().__init__(container)

        self.session = session
        self.show_home = show_home

        self.wiki = Wiki()  

        self.wiki_widget_frame = None

        self.create_frame(session, show_home)

    def create_frame(self, session, entity=0):
        self.check_frame_existence(self.wiki_widget_frame)

        self.wiki_widget_frame = self.select_frame(session, entity)

        self.wiki_widget_frame.grid(row=0, column=0, sticky="NSEW")
        self.wiki_widget_frame.columnconfigure(0, weight=1)

        for child in self.wiki_widget_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def select_frame(self, session, entity=0) -> Union[WikiHome, WikiSection, WikiChapter, CreateCategory]:
        single_call = ('home', 'create_category', 'create_section', 'create_chapter', 'create_topic')

        frames = {
            'home': WikiHome,
            'category': 0,
            'section': WikiSection,
            'chapter': WikiChapter,
            'create_category': CreateCategory,
            'create_section': 0,
            'create_chapter': 0,
            'create_topic': 0

        }

        selected_frame = frames[session]

        if session in single_call:
            return selected_frame(self, self.wiki, self.show_home)

        return selected_frame(self, entity, self.show_home)

    def check_frame_existence(self, frame):
        if frame is not None and frame.winfo_exists():
            frame.destroy()
