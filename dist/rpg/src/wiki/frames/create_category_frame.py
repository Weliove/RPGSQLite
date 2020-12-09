import tkinter as tk
from tkinter import ttk


class CreateCategoryFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

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

        description_label = ttk.Label(
            self,
            text='Description'
        )
        description_label.grid(row=1, column=0)

        self.description_entry = tk.Text(
            self,
            width=1,
            height=8
        )
        self.description_entry.grid(row=1, column=1)
