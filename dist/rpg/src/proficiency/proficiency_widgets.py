import tkinter as tk
from tkinter import ttk, font


class ProficiencyWidget(ttk.Frame):
    def __init__(self, container, proficiency_frame_number):
        super().__init__(container)

        # --- Attributes ---
        self.proficiency = 'Proficiency ' + proficiency_frame_number

        # --- Widgets ---
        self.name = tk.StringVar()
        self.description_entry = tk.Text()

        # --- Frame ---
        proficiency_widget_frame = ttk.Frame(self)
        proficiency_widget_frame.grid(row=0, column=0, sticky="NSEW")
        proficiency_widget_frame.columnconfigure((0, 1), weight=1)

        self.create_widgets(proficiency_widget_frame)

        for child in proficiency_widget_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def create_widgets(self, container):
        # --- Proficiency ---

        proficiency_label = ttk.Label(
            container,
            text=self.proficiency
        )
        proficiency_label.grid(row=0, column=0, sticky="EW")

        proficiency_separator = ttk.Separator(
            container
        )
        proficiency_separator.grid(row=1, column=0, columnspan=3, sticky="EW")

        # --- Name ---

        name_label = ttk.Label(
            container,
            text="Name"
        )
        name_label.grid(row=2, column=0, sticky="EW")

        name_entry = ttk.Entry(
            container,
            textvariable=self.name,
            width=60
        )
        name_entry.grid(row=2, column=1, sticky="EW")

        # --- Description ---
        description_label = ttk.Label(
            container,
            text="Description"
        )
        description_label.grid(row=3, column=0, sticky="EW")

        self.description_entry = tk.Text(
            container,
            width=1,
            height=5
        )
        self.description_entry.grid(row=3, column=1, sticky="EW")

        description_scroll = ttk.Scrollbar(
            container,
            orient="vertical",
            command=self.description_entry.yview
        )
        description_scroll.grid(row=3, column=2, sticky="ns")

        self.description_entry["yscrollcommand"] = description_scroll.set

        self.description_entry.insert(tk.END, 'None')
