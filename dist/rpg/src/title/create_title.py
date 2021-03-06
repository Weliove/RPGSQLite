import tkinter as tk
from tkinter import ttk

from src.popup_info import popup_showinfo
from src.title.title import Title
from src.title.title_widget import TitleWidget


class CreateTitle(ttk.Frame):
    def __init__(self, parent, show_home):
        super().__init__(parent)

        self.show_home = show_home

        # --- Create Widget Frame ---
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.create_title_scroll = TitleScroll(self)
        self.create_title_scroll.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

        self.create_title_scroll.create_title_container()


class TitleScroll(tk.Canvas):
    def __init__(self, container):
        super().__init__(container, highlightthickness=0)

        # --- Custom ---

        self.container = container

        self.title_frames = []
        self.title_buttons = ttk.Frame()
        self.title_widgets_frame = None

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

    def create_title_container(self):
        # --- Create Widgets ---
        self.title_widgets_frame = TitleWidget(self.screen, '')
        self.title_widgets_frame.grid(row=0, column=0, sticky="NSEW")
        self.title_widgets_frame.columnconfigure(0, weight=1)

        self.title_frames.append(self.title_widgets_frame)

        # --- Create Button Frame ---
        self.title_buttons = ttk.Frame(self.screen)
        self.title_buttons.grid(row=1, column=0, sticky="EW")
        self.title_buttons.columnconfigure(0, weight=1)

        self.create_buttons(self.title_buttons)

        for child in self.title_buttons.winfo_children():
            child.grid_configure(padx=5, pady=5, sticky="EW")

    def create_buttons(self, container):
        parent = self.container

        create_item_button = ttk.Button(
            container,
            text="Create",
            command=self.create_title,
            cursor="hand2"
        )
        create_item_button.grid(row=0, column=0)

        add_title_widgets = ttk.Button(
            container,
            text="Add Title",
            command=self.add_title_frame,
            cursor="hand2"
        )
        add_title_widgets.grid(row=1, column=0)

        back_button = ttk.Button(
            container,
            text="← Back",
            command=parent.show_home,
            cursor="hand2"
        )
        back_button.grid(row=2, column=0)

    def add_title_frame(self):
        current_rows = self.screen.grid_size()[1]
        frame_number = len(self.title_frames) + 1
        title_frame_number = str(frame_number)

        new_title_frame = TitleWidget(self.screen, title_frame_number)
        new_title_frame.grid(row=current_rows - 1, column=0, sticky="NSEW")
        new_title_frame.columnconfigure(0, weight=1)

        self.title_frames.append(new_title_frame)

        self.title_buttons.grid_configure(row=current_rows)

    def create_title(self):
        for title_frame in self.title_frames:
            character = self.handle_selection_change(title_frame.character_entry, title_frame.characters)
            npc = self.handle_selection_change(title_frame.npc_entry, title_frame.npcs)
            monster = self.handle_selection_change(title_frame.monster_entry, title_frame.monsters)

            users = character + npc + monster

            name = title_frame.name.get()
            requirements = self.get_text_data(title_frame.requirements_entry)
            description = self.get_text_data(title_frame.description_entry)

            title = Title(name, requirements, description, users)

            create_title = title.create_title()

            if not create_title:
                self.container.show_home()
            else:
                popup_showinfo(create_title)

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
