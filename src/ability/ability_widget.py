import tkinter as tk
from tkinter import ttk, font

from src.connection.database import get_search_entities
from src.ability.ability_property import get_items_names


class AbilityWidget(ttk.Frame):
    def __init__(self, container, ability_frame_number):
        super().__init__(container)

        self.font = font.Font(size=11)

        self.types_ = ('None', 'Character', 'NPC', 'Monster')

        self.characters = ['None', 'Character'] + get_search_entities('', 'Character')
        self.npcs = ['None', 'NPC'] + get_search_entities('', 'NPC')
        self.monsters = ['None', 'Monster'] + get_search_entities('', 'Monster')
        self.items = ['None', 'Item'] + get_items_names()

        # --- Attributes ---
        self.ability = 'Ability ' + ability_frame_number
        self.name = tk.StringVar()
        self.casting = tk.StringVar(value='None')
        self.components = tk.StringVar(value='None')

        self.character = tk.StringVar(value=self.characters[1])
        self.npc = tk.StringVar(value=self.npcs[0])
        self.monster = tk.StringVar(value=self.monsters[0])
        self.item = tk.StringVar(value=self.items[0])

        # --- Widgets ---
        self.character_menu = ttk.Combobox()
        self.npc_menu = ttk.Combobox()
        self.monster_menu = ttk.Combobox()
        self.item_menu = ttk.Combobox()

        self.requirements_entry = tk.Text()
        self.conditions_entry = tk.Text()
        self.effects_entry = tk.Text()
        self.description_entry = tk.Text()

        # --- Frame ---
        ability_widget_frame = ttk.Frame(self)
        ability_widget_frame.grid(row=0, column=0, sticky="NSEW")
        ability_widget_frame.columnconfigure((0, 1), weight=1)

        self.create_widgets(ability_widget_frame)

        for child in ability_widget_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def create_widgets(self, container):
        # --- Ability ---

        ability_label = ttk.Label(
            container,
            text=self.ability
        )
        ability_label.grid(row=0, column=0, sticky="EW")

        ability_separator = ttk.Separator(
            container
        )
        ability_separator.grid(row=1, column=0, columnspan=3, sticky="EW")

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

        # --- User ---

        user_label = ttk.Label(
            container,
            text="User"
        )
        user_label.grid(row=3, column=0, sticky="EW")

        self.character_menu = ttk.Combobox(
            container,
            name='character',
            textvariable=self.character,
            values=self.characters,
            state="readonly"
        )
        self.character_menu.grid(row=3, column=1, sticky="EW")

        # --- NPC ---

        self.npc_menu = ttk.Combobox(
            container,
            name='npc',
            textvariable=self.npc,
            values=self.npcs,
            state="readonly"
        )
        self.npc_menu.grid(row=4, column=1, sticky="EW")

        # --- Monster ---

        self.monster_menu = ttk.Combobox(
            container,
            name='monster',
            textvariable=self.monster,
            values=self.monsters,
            state="readonly"
        )
        self.monster_menu.grid(row=5, column=1, sticky="EW")

        # --- Item ---

        self.item_menu = ttk.Combobox(
            container,
            name='item',
            textvariable=self.item,
            values=self.items,
            state="readonly"
        )
        self.item_menu.grid(row=6, column=1, sticky="EW")

        self.character_menu.bind("<<ComboboxSelected>>", self.selected_value)
        self.npc_menu.bind("<<ComboboxSelected>>", self.selected_value)
        self.monster_menu.bind("<<ComboboxSelected>>", self.selected_value)
        self.item_menu.bind("<<ComboboxSelected>>", self.selected_value)

        # --- Casting ---

        casting_label = ttk.Label(
            container,
            text="Casting"
        )
        casting_label.grid(row=7, column=0, sticky="EW")

        casting_entry = ttk.Entry(
            container,
            textvariable=self.casting,
            width=60
        )
        casting_entry.grid(row=7, column=1, sticky="EW")

        # --- Components ---

        components_label = ttk.Label(
            container,
            text="Components"
        )
        components_label.grid(row=8, column=0, sticky="EW")

        components_entry = ttk.Entry(
            container,
            textvariable=self.components,
            width=60
        )
        components_entry.grid(row=8, column=1, sticky="EW")

        # --- Requirements ---

        requirements_label = ttk.Label(
            container,
            text="Requirements"
        )
        requirements_label.grid(row=9, column=0, sticky="EW")

        self.requirements_entry = tk.Text(
            container,
            width=1,
            height=3
        )
        self.requirements_entry.grid(row=9, column=1, sticky="EW")

        requirements_scroll = ttk.Scrollbar(
            container,
            orient="vertical",
            command=self.requirements_entry.yview
        )
        requirements_scroll.grid(row=9, column=2, sticky="ns")

        self.requirements_entry["yscrollcommand"] = requirements_scroll.set

        self.requirements_entry.insert(tk.END, 'None')

        # --- Conditions ---

        conditions_label = ttk.Label(
            container,
            text="Conditions"
        )
        conditions_label.grid(row=10, column=0, sticky="EW")

        self.conditions_entry = tk.Text(
            container,
            width=1,
            height=3
        )
        self.conditions_entry.grid(row=10, column=1, sticky="EW")

        conditions_scroll = ttk.Scrollbar(
            container,
            orient="vertical",
            command=self.conditions_entry.yview
        )
        conditions_scroll.grid(row=10, column=2, sticky="ns")

        self.conditions_entry["yscrollcommand"] = conditions_scroll.set

        self.conditions_entry.insert(tk.END, 'None')

        # --- Effects ---

        effects_label = ttk.Label(
            container,
            text="Effects"
        )
        effects_label.grid(row=11, column=0, sticky="EW")

        self.effects_entry = tk.Text(
            container,
            width=1,
            height=5
        )
        self.effects_entry.grid(row=11, column=1, sticky="EW")

        effects_scroll = ttk.Scrollbar(
            container,
            orient="vertical",
            command=self.effects_entry.yview
        )
        effects_scroll.grid(row=11, column=2, sticky="ns")

        self.effects_entry["yscrollcommand"] = effects_scroll.set

        self.effects_entry.insert(tk.END, 'None')

        # --- Description ---

        description_label = ttk.Label(
            container,
            text="Description"
        )
        description_label.grid(row=12, column=0, sticky="EW")

        self.description_entry = tk.Text(
            container,
            width=1,
            height=5
        )
        self.description_entry.grid(row=12, column=1, sticky="EW")

        description_scroll = ttk.Scrollbar(
            container,
            orient="vertical",
            command=self.description_entry.yview
        )
        description_scroll.grid(row=12, column=2, sticky="ns")

        self.description_entry["yscrollcommand"] = description_scroll.set

        self.description_entry.insert(tk.END, 'None')

    def selected_value(self, event):
        selected_entity = str(event.widget).split(".")[-1]

        print(selected_entity)

        if selected_entity == 'character':
            self.npc_menu.current(0)
            self.monster_menu.current(0)
            self.item_menu.current(0)
        elif selected_entity == 'npc':
            self.character_menu.current(0)
            self.monster_menu.current(0)
            self.item_menu.current(0)
        elif selected_entity == 'monster':
            self.character_menu.current(0)
            self.npc_menu.current(0)
            self.item_menu.current(0)
        else:
            self.character_menu.current(0)
            self.npc_menu.current(0)
            self.monster_menu.current(0)
