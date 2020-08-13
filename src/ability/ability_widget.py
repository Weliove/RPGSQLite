import tkinter as tk
from tkinter import ttk, font

from src.connection.database import get_search_entities
from src.ability.ability_property import get_items_names


class AbilityWidget(ttk.Frame):
    def __init__(self, container, ability_frame_number):
        super().__init__(container)

        self.font = font.Font(size=11)

        self.types_ = ('None', 'Character', 'NPC', 'Monster')

        self.characters = ['Character'] + get_search_entities('', 'Character')
        self.npcs = ['NPC'] + get_search_entities('', 'NPC')
        self.monsters = ['Monster'] + get_search_entities('', 'Monster')
        self.items = ['Item'] + get_items_names()

        # --- Attributes ---
        self.ability = 'Ability ' + ability_frame_number
        self.name = tk.StringVar()
        self.type_ = tk.StringVar(value=self.types_[0])
        self.casting = tk.StringVar(value='None')
        self.components = tk.StringVar(value='None')

        self.character = tk.StringVar(value=self.characters)
        self.npc = tk.StringVar(value=self.npcs)
        self.monster = tk.StringVar(value=self.monsters)
        self.item = tk.StringVar(value=self.items)

        # --- Widgets ---
        self.character_entry = tk.Listbox()
        self.npc_entry = tk.Listbox()
        self.monster_entry = tk.Listbox()
        self.item_entry = tk.Listbox()
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

        self.character_entry = tk.Listbox(
            container,
            listvariable=self.character,
            # selectmode="extended",
            # exportselection=False,
            selectbackground="#2CCC5B",
            highlightcolor="#1DE557",
            font=self.font,
            width=1,
            height=4
        )
        self.character_entry.grid(row=3, column=1, sticky="EW")

        self.character_entry.select_set(0)

        character_scrollbar = ttk.Scrollbar(container, orient="vertical")
        character_scrollbar.config(command=self.character_entry.yview)
        character_scrollbar.grid(row=3, column=2, sticky="NS")

        self.character_entry.config(yscrollcommand=character_scrollbar.set)

        # --- NPC ---

        self.npc_entry = tk.Listbox(
            container,
            listvariable=self.npc,
            # selectmode="extended",
            # exportselection=False,
            selectbackground="#2CCC5B",
            highlightcolor="#1DE557",
            font=self.font,
            width=1,
            height=4
        )
        self.npc_entry.grid(row=4, column=1, sticky="EW")

        npc_scrollbar = ttk.Scrollbar(container, orient="vertical")
        npc_scrollbar.config(command=self.npc_entry.yview)
        npc_scrollbar.grid(row=4, column=2, sticky="NS")

        self.npc_entry.config(yscrollcommand=npc_scrollbar.set)

        # --- Monster ---

        self.monster_entry = tk.Listbox(
            container,
            listvariable=self.monster,
            # selectmode="extended",
            # exportselection=False,
            selectbackground="#2CCC5B",
            highlightcolor="#1DE557",
            font=self.font,
            width=1,
            height=4
        )
        self.monster_entry.grid(row=5, column=1, sticky="EW")

        monster_scrollbar = ttk.Scrollbar(container, orient="vertical")
        monster_scrollbar.config(command=self.monster_entry.yview)
        monster_scrollbar.grid(row=5, column=2, sticky="NS")

        self.monster_entry.config(yscrollcommand=monster_scrollbar.set)

        # --- Item ---

        self.item_entry = tk.Listbox(
            container,
            listvariable=self.item,
            # selectmode="extended",
            # exportselection=False,
            selectbackground="#2CCC5B",
            highlightcolor="#1DE557",
            font=self.font,
            width=1,
            height=4
        )
        self.item_entry.grid(row=6, column=1, sticky="EW")

        item_scrollbar = ttk.Scrollbar(container, orient="vertical")
        item_scrollbar.config(command=self.item_entry.yview)
        item_scrollbar.grid(row=6, column=2, sticky="NS")

        self.item_entry.config(yscrollcommand=item_scrollbar.set)

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
