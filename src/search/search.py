import tkinter as tk
from tkinter import ttk

from src.connection.database import get_entity
from src.search.search_widgets import SearchWidget


class Search(ttk.Frame):
    def __init__(self, parent, entities_name, type_, show_home):
        super().__init__(parent)

        # --- Create Widget Frame ---
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.search_scroll = SearchScroll(self, entities_name, type_, show_home)
        self.search_scroll.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

        self.search_scroll.search_container()


class SearchScroll(tk.Canvas):
    def __init__(self, container, entities_name, type_, show_home):
        super().__init__(container, highlightthickness=0)

        # --- Custom ---

        self.container = container
        self.entities_name = entities_name
        self.type_ = type_
        self.show_home = show_home

        self.screen = tk.Frame(container)
        self.screen.columnconfigure(0, weight=1)

        self.search_widgets_frame = SearchWidget(self, self.screen, entities_name, show_home)

        self.scrollable_window = self.create_window((0, 0), window=self.screen, anchor="nw")

        def configure_scroll_region(event):
            self.configure(scrollregion=self.bbox("all"))

        def configure_window_size(event):
            self.itemconfig(self.scrollable_window, width=self.winfo_width())

        self.bind("<Configure>", configure_window_size)
        self.screen.bind("<Configure>", configure_scroll_region)

        scrollbar = ttk.Scrollbar(container, orient="vertical", command=self.yview)
        scrollbar.grid(row=0, column=1, sticky="NS")

        self.configure(yscrollcommand=scrollbar.set)
        self.yview_moveto(1.0)

    def search_container(self):
        # --- Create Widgets ---
        self.search_widgets_frame = SearchWidget(self, self.screen, self.entities_name, self.show_home)
        self.search_widgets_frame.grid(row=0, column=0, sticky="NSEW")
        self.search_widgets_frame.columnconfigure(0, weight=1)

    def search_result(self, entity_name):
        print(get_entity(entity_name, self.type_))
