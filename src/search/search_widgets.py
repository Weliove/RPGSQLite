import tkinter as tk
from tkinter import ttk


class SearchWidget(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        # --- Frame ---
        search_widget_frame = ttk.Frame(self)
        search_widget_frame.grid(row=0, column=0, sticky="NSEW")
        search_widget_frame.columnconfigure((0, 1), weight=1)

        self.create_widgets(search_widget_frame)

        for child in search_widget_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def create_widgets(self, container):
        pass
