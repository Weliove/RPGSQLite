import tkinter as tk
from tkinter import ttk

from src.popup_info import popup_showinfo
from src.proficiency.proficiency import Proficiency
from src.proficiency.proficiency_widgets import ProficiencyWidget


class CreateProficiency(ttk.Frame):
    def __init__(self, parent, show_home):
        super().__init__(parent)

        self.show_home = show_home

        # --- Create Widget Frame ---
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.create_proficiency_scroll = ProficiencyScroll(self)
        self.create_proficiency_scroll.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

        self.create_proficiency_scroll.create_proficiency_container()


class ProficiencyScroll(tk.Canvas):
    def __init__(self, container):
        super().__init__(container, highlightthickness=0)

        # --- Custom ---

        self.container = container

        self.proficiency_frames = []
        self.proficiency_buttons = ttk.Frame()
        self.proficiency_widgets_frame = None

        self.screen = tk.Frame(container)
        self.screen.columnconfigure(0, weight=1)

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

    def create_proficiency_container(self):
        # --- Create Widgets ---
        self.proficiency_widgets_frame = ProficiencyWidget(self.screen, '')
        self.proficiency_widgets_frame.grid(row=0, column=0, sticky="NSEW")
        self.proficiency_widgets_frame.columnconfigure(0, weight=1)

        self.proficiency_frames.append(self.proficiency_widgets_frame)

        # --- Create Button Frame ---
        self.proficiency_buttons = ttk.Frame(self.screen)
        self.proficiency_buttons.grid(row=1, column=0, sticky="EW")
        self.proficiency_buttons.columnconfigure(0, weight=1)

        self.create_buttons(self.proficiency_buttons)

        for child in self.proficiency_buttons.winfo_children():
            child.grid_configure(padx=5, pady=5, sticky="EW")

    def create_buttons(self, container):
        parent = self.container

        create_proficiency_button = ttk.Button(
            container,
            text="Create",
            command=self.create_proficiency,
            cursor="hand2"
        )
        create_proficiency_button.grid(row=0, column=0)

        add_proficiency_widgets = ttk.Button(
            container,
            text="Add Proficiency",
            command=self.add_proficiency_frame,
            cursor="hand2"
        )
        add_proficiency_widgets.grid(row=1, column=0)

        back_button = ttk.Button(
            container,
            text="← Back",
            command=parent.show_home,
            cursor="hand2"
        )
        back_button.grid(row=2, column=0)

    def add_proficiency_frame(self):
        current_rows = self.screen.grid_size()[1]
        frame_number = len(self.proficiency_frames) + 1
        proficiency_frame_number = str(frame_number)

        new_proficiency_frame = ProficiencyWidget(self.screen, proficiency_frame_number)
        new_proficiency_frame.grid(row=current_rows - 1, column=0, sticky="NSEW")
        new_proficiency_frame.columnconfigure(0, weight=1)

        self.proficiency_frames.append(new_proficiency_frame)

        self.proficiency_buttons.grid_configure(row=current_rows)

    def create_proficiency(self):
        for proficiency_frame in self.proficiency_frames:
            name = proficiency_frame.name.get()
            description = self.get_text_data(proficiency_frame.description_entry)

            proficiency = Proficiency(name, description)

            create_proficiency = proficiency.create_proficiency()

            self.container.show_home() if not create_proficiency else popup_showinfo(create_proficiency)

    def get_text_data(self, text_widget):
        return text_widget.get("1.0", 'end-1c')
