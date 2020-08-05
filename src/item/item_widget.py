import tkinter as tk
from tkinter import ttk, font

from src.connection.database import get_search_entities


class ItemWidget(ttk.Frame):
    def __init__(self, container, item_frame_number):
        super().__init__(container)

        self.font = font.Font(size=11)

        characters = ['None'] + get_search_entities('', 'Character')
        npcs = ['None'] + get_search_entities('', 'NPC')
        monsters = ['None'] + get_search_entities('', 'Monster')

        abilities = ['None'] + get_search_entities('', 'Ability')

        # --- Attributes ---

        self.item = 'Item ' + item_frame_number
        self.name = tk.StringVar()
        self.reduction = tk.StringVar(value='0')
        self.damage = tk.StringVar(value='0')
        self.range = tk.StringVar(value='0')
        self.health = tk.StringVar(value='0')
        self.area = tk.StringVar(value='0')

        self.characters = tk.StringVar(value=characters)
        self.npcs = tk.StringVar(value=npcs)
        self.monsters = tk.StringVar(value=monsters)
        self.abilities = tk.StringVar(value=abilities)

        # --- Widgets ---
        self.character_entry = tk.Listbox()
        self.npc_entry = tk.Listbox()
        self.monster_entry = tk.Listbox()
        self.abilities_entry = tk.Listbox()
        self.effects_entry = tk.Text()
        self.description_entry = tk.Text()

        # --- Frame ---
        item_widget_frame = ttk.Frame(self)
        item_widget_frame.grid(row=0, column=0, sticky="NSEW")
        item_widget_frame.columnconfigure((0, 1), weight=1)

        self.create_widgets(item_widget_frame)

        for child in item_widget_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def create_widgets(self, container):
        # --- Item ---

        item_label = ttk.Label(
            container,
            text=self.item
        )
        item_label.grid(row=0, column=0, sticky="EW")

        item_separator = ttk.Separator(
            container
        )
        item_separator.grid(row=1, column=0, columnspan=3, sticky="EW")

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

        # --- Character ---

        character_label = ttk.Label(
            container,
            text="Character"
        )
        character_label.grid(row=3, column=0, sticky="EW")

        self.character_entry = tk.Listbox(
            container,
            listvariable=self.characters,
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

        npc_label = ttk.Label(
            container,
            text="NPC"
        )
        npc_label.grid(row=4, column=0, sticky="EW")

        self.npc_entry = tk.Listbox(
            container,
            listvariable=self.npcs,
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

        monster_label = ttk.Label(
            container,
            text="Monster"
        )
        monster_label.grid(row=5, column=0, sticky="EW")

        self.monster_entry = tk.Listbox(
            container,
            listvariable=self.monsters,
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

        # --- Type ---

        type_label = ttk.Label(
            container,
            text="Type"
        )
        type_label.grid(row=6, column=0, sticky="EW")

        type_entry = ttk.Combobox(
            container
        )
        type_entry.grid(row=6, column=1, sticky="EW")

        # --- Reduction ---

        reduction_label = ttk.Label(
            container,
            text="Reduction"
        )
        reduction_label.grid(row=7, column=0, sticky="EW")

        reduction_entry = ttk.Entry(
            container,
            textvariable=self.reduction,
            width=60
        )
        reduction_entry.grid(row=7, column=1, sticky="EW")

        # --- Damage ---

        damage_label = ttk.Label(
            container,
            text="Damage"
        )
        damage_label.grid(row=8, column=0, sticky="EW")

        damage_entry = ttk.Entry(
            container,
            textvariable=self.damage,
            width=60
        )
        damage_entry.grid(row=8, column=1, sticky="EW")

        # --- Range ---

        range_label = ttk.Label(
            container,
            text="Range"
        )
        range_label.grid(row=9, column=0, sticky="EW")

        range_entry = ttk.Entry(
            container,
            textvariable=self.range,
            width=60
        )
        range_entry.grid(row=9, column=1, sticky="EW")

        # --- Health ---

        health_label = ttk.Label(
            container,
            text="Health"
        )
        health_label.grid(row=10, column=0, sticky="EW")

        health_entry = ttk.Entry(
            container,
            textvariable=self.health,
            width=60
        )
        health_entry.grid(row=10, column=1, sticky="EW")

        # --- Area ---

        area_label = ttk.Label(
            container,
            text="Area"
        )
        area_label.grid(row=11, column=0, sticky="EW")

        area_entry = ttk.Entry(
            container,
            textvariable=self.area,
            width=60
        )
        area_entry.grid(row=11, column=1, sticky="EW")

        # --- Abilities ---

        abilities_label = ttk.Label(
            container,
            text="Abilities"
        )
        abilities_label.grid(row=12, column=0, sticky="EW")

        self.abilities_entry = tk.Listbox(
            container,
            listvariable=self.abilities,
            selectmode="extended",
            exportselection=False,
            selectbackground="#2CCC5B",
            highlightcolor="#1DE557",
            font=self.font,
            width=1,
            height=5
        )
        self.abilities_entry.grid(row=12, column=1, sticky="EW")

        self.abilities_entry.select_set(0)

        abilities_scrollbar = ttk.Scrollbar(container, orient="vertical")
        abilities_scrollbar.config(command=self.abilities_entry.yview)
        abilities_scrollbar.grid(row=12, column=2, sticky="NS")

        self.abilities_entry.config(yscrollcommand=abilities_scrollbar.set)

        # --- Effects ---

        effects_label = ttk.Label(
            container,
            text="Effects"
        )
        effects_label.grid(row=13, column=0, sticky="EW")

        self.effects_entry = tk.Text(
            container,
            width=1,
            height=5
        )
        self.effects_entry.grid(row=13, column=1, sticky="EW")

        effects_scroll = ttk.Scrollbar(
            container,
            orient="vertical",
            command=self.effects_entry.yview
        )
        effects_scroll.grid(row=13, column=2, sticky="ns")

        self.effects_entry["yscrollcommand"] = effects_scroll.set

        self.effects_entry.insert(tk.END, 'None')

        # --- Description ---

        description_label = ttk.Label(
            container,
            text="Description"
        )
        description_label.grid(row=14, column=0, sticky="EW")

        self.description_entry = tk.Text(
            container,
            width=1,
            height=5
        )
        self.description_entry.grid(row=14, column=1, sticky="EW")

        description_scroll = ttk.Scrollbar(
            container,
            orient="vertical",
            command=self.description_entry.yview
        )
        description_scroll.grid(row=14, column=2, sticky="ns")

        self.description_entry["yscrollcommand"] = description_scroll.set

        self.description_entry.insert(tk.END, 'None')