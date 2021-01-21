from tkinter import ttk
from typing import Union

from src.wiki.create_category import CreateCategory
from src.wiki.create_chapter import CreateChapter
from src.wiki.create_section import CreateSection
from src.wiki.create_topic import CreateTopic
from src.wiki.edit.wiki_edit import WikiEdit
from src.wiki.wiki import Wiki
from src.wiki.wiki_chapter import WikiChapter
from src.wiki.wiki_home import WikiHome
from src.wiki.wiki_section import WikiSection


class WikiWidget(ttk.Frame):
    def __init__(self, parent, container, session, show_home):
        super().__init__(container)

        self.parent = parent
        self.session = session
        self.show_home = show_home

        self.wiki = Wiki()

        self.wiki_widget_frame = None

        self.create_frame(session, show_home)

    def create_frame(self, session, entity=0):
        self.check_frame_existence(self.wiki_widget_frame)

        self.wiki_widget_frame = self.select_frame(session, entity)
        self.wiki_widget_frame.grid(row=0, column=0, sticky='NSEW')
        self.wiki_widget_frame.columnconfigure(0, weight=1)

        for child in self.wiki_widget_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

        self.parent.yview_moveto(0)

    def select_frame(self, session, entity=None) -> Union[WikiHome, WikiSection, WikiChapter, CreateCategory,
                                                          CreateSection, CreateChapter, CreateTopic]:
        single_call = (
            'section',
            'chapter',
            'create_topic'
        )

        create_call = (
            'home',
            'create_category',
            'create_section',
            'create_chapter',
            'edit'
        )

        frames = {
            'home': WikiHome,
            'category': None,
            'section': WikiSection,
            'chapter': WikiChapter,
            'edit': WikiEdit,
            'create_category': CreateCategory,
            'create_section': CreateSection,
            'create_chapter': CreateChapter,
            'create_topic': CreateTopic
        }

        selected_frame = frames[session]

        if session in create_call:
            return selected_frame(self, self.wiki)
        elif session in single_call:
            return selected_frame(self, entity, self.wiki)

        return selected_frame(self, entity)

    def check_frame_existence(self, frame):
        if frame is not None and frame.winfo_exists():
            frame.destroy()
