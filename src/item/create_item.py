import tkinter as tk
from tkinter import ttk

from src.item.item_widget import ItemWidget


class CreateItem(ttk.Frame):
    def __init__(self, parent, show_home):
        super().__init__(parent)

        self.show_home = show_home

        # --- Create Widget Frame ---
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.create_item_scroll = ItemScroll(self)
        self.create_item_scroll.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

        self.create_item_scroll.create_item_container()


class ItemScroll(tk.Canvas):
    def __init__(self, container):
        super().__init__(container, highlightthickness=0)

        # --- Custom ---

        self.container = container

        self.item_frames = []
        self.item_buttons = ttk.Frame()
        self.item_widgets_frame = None

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

    def create_item_container(self):
        # --- Create Widgets ---
        self.item_widgets_frame = ItemWidget(self.screen, '')
        self.item_widgets_frame.grid(row=0, column=0, sticky="NSEW")
        self.item_widgets_frame.columnconfigure(0, weight=1)

        self.item_frames.append(self.item_widgets_frame)

        # --- Create Button Frame ---
        self.item_buttons = ttk.Frame(self.screen)
        self.item_buttons.grid(row=1, column=0, sticky="EW")
        self.item_buttons.columnconfigure(0, weight=1)

        self.create_buttons(self.item_buttons)

        for child in self.item_buttons.winfo_children():
            child.grid_configure(padx=5, pady=5, sticky="EW")

    def create_buttons(self, container):
        parent = self.container

        create_avatar_button = ttk.Button(
            container,
            text="Create",
            command=self.create_item,
            cursor="hand2"
        )
        create_avatar_button.grid(row=0, column=0)

        add_item_widgets = ttk.Button(
            container,
            text="Add Item Widgets",
            command=lambda: self.add_item_frame(),
            cursor="hand2"
        )
        add_item_widgets.grid(row=1, column=0)

        back_button = ttk.Button(
            container,
            text="← Back",
            command=parent.show_home,
            cursor="hand2"
        )
        back_button.grid(row=2, column=0)

    def add_item_frame(self):
        current_rows = self.screen.grid_size()[1]
        item_frame_number = str(len(self.item_frames) + 1)

        new_item_frame = ItemWidget(self.screen, item_frame_number)
        new_item_frame.grid(row=current_rows - 1, column=0, sticky="NSEW")
        new_item_frame.columnconfigure(0, weight=1)
        self.item_frames.append(new_item_frame)

        self.item_buttons.grid_configure(row=current_rows)

    def create_item(self):
        pass

    def handle_selection_change(self, list_widget, total_list):
        selected_indices = list_widget.curselection()
        result_list = []

        if len(selected_indices) == 0 or (len(selected_indices) == 1 and selected_indices[0] == 'None'):
            return []

        for i in selected_indices:
            result_list.append(total_list[i])

        return result_list

    def get_text_data(self, text_widget):
        return text_widget.get("1.0", 'end-1c')
