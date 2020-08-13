import tkinter as tk
from tkinter import ttk

from src.interface.interface_widgets import InterfaceWidget


class Interface(ttk.Frame):
    def __init__(self, parent, entity, type_, show_search, show_home):
        super().__init__(parent)

        # --- Create Widget Frame ---
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.interface_scroll = InterfaceScroll(self)
        self.interface_scroll.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

        self.interface_scroll.interface_container(entity, type_, show_search, show_home)


class InterfaceScroll(tk.Canvas):
    def __init__(self, container):
        super().__init__(container, highlightthickness=0)

        # --- Custom ---

        self.container = container

        self.screen = tk.Frame(container)
        self.screen.columnconfigure(0, weight=1)

        self.interface_widgets_frame = None

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

    def interface_container(self, entity, type_, show_search, show_home):
        # --- Create Widgets ---
        self.interface_widgets_frame = InterfaceWidget(self.screen, entity, type_, show_search, show_home)
        self.interface_widgets_frame.grid(row=0, column=0, sticky="NSEW")
        self.interface_widgets_frame.columnconfigure(0, weight=1)
