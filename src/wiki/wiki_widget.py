from tkinter import ttk

from src.wiki.wiki_chapter import WikiChapter
from src.wiki.wiki_home import WikiHome
from src.wiki.wiki_section import WikiSection


class WikiWidget(ttk.Frame):
    def __init__(self, container, session, show_home):
        super().__init__(container)

        self.session = session
        self.show_home = show_home

        self.wiki_widget_frame = None

        self.create_frame(session, show_home)

    def create_frame(self, session, entity=0):
        self.check_frame_existence(self.wiki_widget_frame)

        if session == 'home':
            self.wiki_widget_frame = WikiHome(self, self.show_home)
        elif session == 'category':
            pass
        elif session == 'section':
            self.wiki_widget_frame = WikiSection(self, entity, self.show_home)
        elif session == 'chapter':
            self.wiki_widget_frame = WikiChapter(self, entity, self.show_home)
        elif session == 'create_category':
            pass
        elif session == 'create_section':
            pass
        elif session == 'create_chapter':
            pass
        elif session == 'create_topic':
            pass

        self.wiki_widget_frame.grid(row=0, column=0, sticky="NSEW")
        self.wiki_widget_frame.columnconfigure(0, weight=1)

        for child in self.wiki_widget_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def check_frame_existence(self, frame):
        if frame is not None and frame.winfo_exists():
            frame.destroy()
