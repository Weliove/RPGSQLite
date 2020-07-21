import tkinter as tk
from tkinter import ttk

from src.avatar.avatar import Avatar
from src.avatar.avatar_widget import AvatarWidget


class CreateAvatar(ttk.Frame):
    def __init__(self, parent, show_home):
        super().__init__(parent)

        self.show_home = show_home

        # --- Create Widget Frame ---
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.create_avatar_scroll = AvatarScroll(self)
        self.create_avatar_scroll.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

        self.create_avatar_scroll.create_avatar_container()


class AvatarScroll(tk.Canvas):
    def __init__(self, container):
        super().__init__(container, highlightthickness=0)

        # --- Custom ---

        self.container = container

        self.screen = tk.Frame(container)
        self.screen.columnconfigure(0, weight=1)

        self.avatar_widgets_frame = None

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

    def create_avatar_container(self):
        # --- Create Widgets ---
        self.avatar_widgets_frame = AvatarWidget(self.screen)
        self.avatar_widgets_frame.grid(row=0, column=0, sticky="NSEW")
        self.avatar_widgets_frame.columnconfigure(0, weight=1)

        # --- Create Button Frame ---
        avatar_buttons = ttk.Frame(self.screen)
        avatar_buttons.grid(row=1, column=0, sticky="EW")
        avatar_buttons.columnconfigure(0, weight=1)

        self.create_buttons(avatar_buttons)

        for child in avatar_buttons.winfo_children():
            child.grid_configure(padx=5, pady=5, sticky="EW")

    def create_buttons(self, container):
        parent = self.container

        create_avatar_button = ttk.Button(
            container,
            text="Create",
            command=self.create_avatar,
            cursor="hand2"
        )
        create_avatar_button.grid(row=0, column=0)

        back_button = ttk.Button(
            container,
            text="← Back",
            command=parent.show_home,
            cursor="hand2"
        )
        back_button.grid(row=1, column=0)

    def create_avatar(self):
        widgets = self.avatar_widgets_frame

        name = widgets.name.get()
        type_ = widgets.type.get()
        type_result = widgets.type_values.index(type_) + 1
        health = widgets.health.get()
        adrenaline = widgets.adrenaline.get()
        class_ = widgets.class_.get()
        armor = widgets.armor.get()
        special_armor = widgets.special_armor.get()
        weapon = self.handle_selection_change(widgets.weapon_entry, widgets.weapons)
        special_weapon = self.handle_selection_change(widgets.weapon_special_entry, widgets.special_weapons)
        physical_ability = widgets.physical_ability.get()
        title = self.handle_selection_change(widgets.title_entry, widgets.titles)
        ability = self.handle_selection_change(widgets.ability_entry, widgets.abilities)
        proficiency = self.handle_selection_change(widgets.proficiency_entry, widgets.proficiencies)
        description = self.get_text_data(widgets.description_entry)

        avatar = Avatar(name, type_result, health, adrenaline, class_, armor, weapon,
                        physical_ability, title, ability, proficiency, description)

        if type_ == 'Character':
            avatar.create_character()
        else:
            avatar.create_monster()

    def handle_selection_change(self, list_widget, total_list):
        selected_indices = list_widget.curselection()
        result_list = []

        for i in selected_indices:
            result_list.append(total_list[i])

        return tuple(result_list)

    def get_text_data(self, text_widget):
        return text_widget.get("1.0", 'end-1c')
