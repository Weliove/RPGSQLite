import tkinter as tk
from tkinter import ttk

from src.search.search_widgets import SearchWidget


class Search(ttk.Frame):
    def __init__(self, parent, show_home):
        super().__init__(parent)

        self.show_home = show_home

        # --- Create Widget Frame ---
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.search_scroll = SearchScroll(self)
        self.search_scroll.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

        self.search_scroll.search_container()


class SearchScroll(tk.Canvas):
    def __init__(self, container):
        super().__init__(container, highlightthickness=0)

        # --- Custom ---

        self.container = container

        self.screen = tk.Frame(container)
        self.screen.columnconfigure(0, weight=1)

        self.search_widgets_frame = SearchWidget(self.screen)

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
        self.search_widgets_frame = SearchWidget(self.screen)
        self.search_widgets_frame.grid(row=0, column=0, sticky="NSEW")
        self.search_widgets_frame.columnconfigure(0, weight=1)

        # --- Create Button Frame ---
        search_buttons = ttk.Frame(self.screen)
        search_buttons.grid(row=1, column=0, sticky="EW")
        search_buttons.columnconfigure(0, weight=1)

        self.create_buttons(search_buttons)

        for child in search_buttons.winfo_children():
            child.grid_configure(padx=5, pady=5, sticky="EW")

    def create_buttons(self, container):
        parent = self.container

        choose_entity_button = ttk.Button(
            container,
            text="Create",
            # command=self.create_avatar,
            cursor="hand2"
        )
        choose_entity_button.grid(row=0, column=0)

        back_button = ttk.Button(
            container,
            text="← Back",
            command=parent.show_home,
            cursor="hand2"
        )
        back_button.grid(row=1, column=0)
