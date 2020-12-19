import tkinter as tk
from tkinter import ttk, font

from src.connection.database import get_search_entities
from src.connection.handle_abilities import get_abilities_name_by_type


class ItemWidget(ttk.Frame):
    def __init__(self, container, item_frame_number):
        super().__init__(container)

        self.font = font.Font(size=11)

        self.types_ = ('Armor', 'Weapon')

        self.characters = ['None', 'Character'] + get_search_entities('', 'Character')
        self.npcs = ['None', 'NPC'] + get_search_entities('', 'NPC')
        self.monsters = ['None', 'Monster'] + get_search_entities('', 'Monster')

        self.abilities = ['None', 'Ability'] + get_abilities_name_by_type(4)

        # --- Attributes ---
        self.item = 'Item ' + item_frame_number
        self.name = tk.StringVar()
        self.type_ = tk.StringVar(value=self.types_[0])
        self.reduction = tk.StringVar(value='0')
        self.damage = tk.StringVar(value='0')
        self.range_ = tk.StringVar(value='0')
        self.health = tk.StringVar(value='0')
        self.area = tk.StringVar(value='0')

        self.character = tk.StringVar(value=self.characters[1])
        self.npc = tk.StringVar(value=self.npcs[0])
        self.monster = tk.StringVar(value=self.monsters[0])
        self.ability = tk.StringVar(value=self.abilities)

        # --- Widgets ---
        self.character_menu = ttk.Combobox()
        self.npc_menu = ttk.Combobox()
        self.monster_menu = ttk.Combobox()

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

        self.character_menu.bind("<<ComboboxSelected>>", self.selected_value)
        self.npc_menu.bind("<<ComboboxSelected>>", self.selected_value)
        self.monster_menu.bind("<<ComboboxSelected>>", self.selected_value)

        # --- Type ---

        type_label = ttk.Label(
            container,
            text="Type"
        )
        type_label.grid(row=6, column=0, sticky="EW")

        type_entry = ttk.Combobox(
            container,
            textvariable=self.type_,
            values=self.types_,
            exportselection=False,
            state="readonly"
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
            textvariable=self.range_,
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
            listvariable=self.ability,
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

    def selected_value(self, event):
        selected_entity = str(event.widget).split(".")[-1]

        print(selected_entity)

        if selected_entity == 'character':
            self.npc_menu.current(0)
            self.monster_menu.current(0)
        elif selected_entity == 'npc':
            self.character_menu.current(0)
            self.monster_menu.current(0)
        elif selected_entity == 'monster':
            self.character_menu.current(0)
            self.npc_menu.current(0)
