import re
import tkinter as tk
from tkinter import ttk
import tkinter.font as font

from src.ability.ability_widget import AbilityWidget


class CreateAbility(ttk.Frame):
    def __init__(self, parent, show_home):
        super().__init__(parent)

        self.show_home = show_home

        # --- Create Widget Frame ---
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.create_ability_scroll = AbilityScroll(self)
        self.create_ability_scroll.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

        self.create_ability_scroll.create_ability_container()


class AbilityScroll(tk.Canvas):
    def __init__(self, container):
        super().__init__(container, highlightthickness=0)

        # --- Custom ---

        self.container = container

        self.ability_frames = []
        self.ability_buttons = ttk.Frame()
        self.ability_widgets_frame = None

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

    def create_ability_container(self):
        # --- Create Widgets ---
        self.ability_widgets_frame = AbilityWidget(self.screen, '')
        self.ability_widgets_frame.grid(row=0, column=0, sticky="NSEW")
        self.ability_widgets_frame.columnconfigure(0, weight=1)

        self.ability_frames.append(self.ability_widgets_frame)

        # --- Create Button Frame ---
        self.ability_buttons = ttk.Frame(self.screen)
        self.ability_buttons.grid(row=1, column=0, sticky="EW")
        self.ability_buttons.columnconfigure(0, weight=1)

        self.create_buttons(self.ability_buttons)

        for child in self.ability_buttons.winfo_children():
            child.grid_configure(padx=5, pady=5, sticky="EW")

    def create_buttons(self, container):
        parent = self.container

        create_ability_button = ttk.Button(
            container,
            text="Create",
            command=self.create_ability,
            cursor="hand2"
        )
        create_ability_button.grid(row=0, column=0)

        add_ability_widgets = ttk.Button(
            container,
            text="Add Ability",
            command=self.add_ability_frame,
            cursor="hand2"
        )
        add_ability_widgets.grid(row=1, column=0)

        back_button = ttk.Button(
            container,
            text="← Back",
            command=parent.show_home,
            cursor="hand2"
        )
        back_button.grid(row=2, column=0)

    def add_ability_frame(self):
        current_rows = self.screen.grid_size()[1]
        frame_number = len(self.ability_frames) + 1
        ability_frame_number = str(frame_number)

        new_ability_frame = AbilityWidget(self.screen, ability_frame_number)
        new_ability_frame.grid(row=current_rows - 1, column=0, sticky="NSEW")
        new_ability_frame.columnconfigure(0, weight=1)

        self.ability_frames.append(new_ability_frame)

        self.ability_buttons.grid_configure(row=current_rows)

    def create_ability(self):
        pass

    def choose_user(self, character, npc, monster):
        user = ''

        if len(character) > 0:
            user = character[0]
        elif len(npc) > 0:
            user = npc[0]
        elif len(monster) > 0:
            user = monster[0]

        return user

    def handle_selection_change(self, list_widget, total_list):
        selected_indices = list_widget.curselection()
        result_list = []

        if len(selected_indices) == 0 or (len(selected_indices) == 1 and total_list[selected_indices[0]] == 'None'):
            return []

        for i in selected_indices:
            result_list.append(total_list[i])

        return result_list

    def get_text_data(self, text_widget):
        return text_widget.get("1.0", 'end-1c')
