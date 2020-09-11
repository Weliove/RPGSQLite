import tkinter as tk
from tkinter import ttk

from src.wiki.wiki_widget import WikiWidget


class CreateWiki(ttk.Frame):
    def __init__(self, parent, show_home):
        super().__init__(parent)

        self.show_home = show_home

        # --- Create Widget Frame ---
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.create_wiki_scroll = WikiScroll(self)
        self.create_wiki_scroll.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

        self.create_wiki_scroll.create_wiki_container()


class WikiScroll(tk.Canvas):
    def __init__(self, container):
        super().__init__(container, highlightthickness=0)

        # --- Custom ---

        self.container = container

        self.wiki_buttons = ttk.Frame()
        self.wiki_widget_frame = None

        self.screen = tk.Frame(container)
        self.screen.columnconfigure(0, weight=1)

        self.scrollable_window = self.create_window((0, 0), window=self.screen, anchor="nw")

        def configure_scroll_region(event):
            self.configure(scrollregion=self.bbox("all"))

        def configure_window_size(event):
            self.itemconfig(self.scrollable_window, width=self.winfo_width())

        self.bind("<Configure>", configure_window_size)
        self.screen.bind("<Configure>", configure_scroll_region)
        self.bind_all("<MouseWheel>", self._on_mouse_wheel)

        scrollbar = ttk.Scrollbar(container, orient="vertical", command=self.yview)
        scrollbar.grid(row=0, column=1, sticky="NS")

        self.configure(yscrollcommand=scrollbar.set)
        self.yview_moveto(1.0)

    def _on_mouse_wheel(self, event):
        self.yview_scroll(-int(event.delta/120), "units")

    def create_wiki_container(self):
        # --- Create Widgets ---
        self.wiki_widget_frame = WikiWidget(self.screen, 'home', self.container.show_home)
        self.wiki_widget_frame.grid(row=0, column=0, sticky="NSEW")
        self.wiki_widget_frame.columnconfigure(0, weight=1)

        # --- Create Button Frame ---
        self.wiki_buttons = ttk.Frame(self.screen)
        self.wiki_buttons.grid(row=1, column=0, sticky="EW")
        self.wiki_buttons.columnconfigure(0, weight=1)

        self.create_buttons(self.wiki_buttons)

        for child in self.wiki_buttons.winfo_children():
            child.grid_configure(padx=5, pady=5, sticky="EW")

    def create_buttons(self, container):
        parent = self.container

        wiki_separator = ttk.Separator(
            container
        )
        wiki_separator.grid(row=0, column=0, columnspan=1, sticky="EW")

        home_button = ttk.Button(
            container,
            text='Home',
            command=parent.show_home,
            cursor='hand2'
        )
        home_button.grid(row=1, column=0, sticky="EW")

    def add_wiki_frame(self):
        current_rows = self.screen.grid_size()[1]

        self.wiki_buttons.grid_configure(row=current_rows)
