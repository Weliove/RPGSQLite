import tkinter as tk
from tkinter import ttk, font

from src.avatar.avatar_properties import *
from src.connection.handle_abilities import get_abilities_by_type


class AvatarWidget(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.font = font.Font(size=11)

        self.type_values = ('Character', 'NPC', 'Monster')

        self.classes_total = get_classes()
        self.classes = ['None'] + get_entities_names(self.classes_total)

        self.armors_total = get_specific_items('', 1)
        self.armors = ['None'] + get_entities_names(self.armors_total)

        self.weapons_total = get_specific_items('', 2)
        self.weapons = ['None'] + get_entities_names(self.weapons_total)

        self.titles_total = get_titles()
        self.titles = ['None'] + get_entities_names(self.titles_total)

        self.abilities_total = get_abilities_by_type(1) + get_abilities_by_type(2) + get_abilities_by_type(3)
        self.abilities = ['None'] + get_entities_names(self.abilities_total)

        self.proficiencies_total = get_proficiencies()
        self.proficiencies = ['None'] + get_entities_names(self.proficiencies_total)

        # --- Attributes ---
        self.name = tk.StringVar()
        self.health = tk.StringVar(value=0)
        self.type = tk.StringVar(value=self.type_values[0])
        self.adrenaline = tk.StringVar(value=0)
        self.class_ = tk.StringVar(value=self.classes)
        self.armor = tk.StringVar(value=self.armors[0])
        self.weapon = tk.StringVar(value=self.weapons)
        self.physical_ability = tk.StringVar(value='None')
        self.title = tk.StringVar(value=self.titles)
        self.ability = tk.StringVar(value=self.abilities)
        self.proficiency = tk.StringVar(value=self.proficiencies)

        # --- Widgets ---
        self.class_entry = tk.Listbox()
        self.weapon_entry = tk.Listbox()
        self.title_entry = tk.Listbox()
        self.ability_entry = tk.Listbox()
        self.proficiency_entry = tk.Listbox()
        self.description_entry = tk.Text()

        # --- Frame ---
        avatar_widget_frame = ttk.Frame(self)
        avatar_widget_frame.grid(row=0, column=0, sticky="NSEW")
        avatar_widget_frame.columnconfigure((0, 1), weight=1)

        self.create_widgets(avatar_widget_frame)

        for child in avatar_widget_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def create_widgets(self, container):
        # --- Name ---
        name_label = ttk.Label(
            container,
            text="Name"
        )
        name_label.grid(row=0, column=0, sticky="EW")

        name_entry = ttk.Entry(
            container,
            textvariable=self.name,
            width=60
        )
        name_entry.grid(row=0, column=1, sticky="EW")

        # --- Type ---
        type_label = ttk.Label(
            container,
            text="Type"
        )
        type_label.grid(row=1, column=0, sticky="EW")

        type_entry = ttk.Combobox(
            container,
            textvariable=self.type,
            values=self.type_values,
            state="readonly"
        )
        type_entry.grid(row=1, column=1, sticky="EW")

        # --- Health ---
        health_label = ttk.Label(
            container,
            text="Health"
        )
        health_label.grid(row=2, column=0, sticky="EW")

        health_entry = ttk.Entry(
            container,
            textvariable=self.health,
            width=60
        )
        health_entry.grid(row=2, column=1, sticky="EW")

        # --- Adrenaline ---
        adrenaline_label = ttk.Label(
            container,
            text="Adrenaline"
        )
        adrenaline_label.grid(row=3, column=0, sticky="EW")

        adrenaline_entry = ttk.Entry(
            container,
            textvariable=self.adrenaline
        )
        adrenaline_entry.grid(row=3, column=1, sticky="EW")

        # --- Class ---
        class_label = ttk.Label(
            container,
            text="Class"
        )
        class_label.grid(row=4, column=0, sticky="EW")

        self.class_entry = tk.Listbox(
            container,
            listvariable=self.class_,
            selectmode="extended",
            exportselection=False,
            selectbackground="#2CCC5B",
            highlightcolor="#1DE557",
            font=self.font,
            width=1,
            height=5
        )
        self.class_entry.grid(row=4, column=1, sticky="EW")

        self.class_entry.select_set(0)

        class_scrollbar = ttk.Scrollbar(container, orient="vertical")
        class_scrollbar.config(command=self.class_entry.yview)
        class_scrollbar.grid(row=4, column=2, sticky="NS")

        self.class_entry.config(yscrollcommand=class_scrollbar.set)

        # --- Armor ---
        armor_label = ttk.Label(
            container,
            text="Armor"
        )
        armor_label.grid(row=5, column=0, sticky="EW")

        armor_entry = ttk.Combobox(
            container,
            textvariable=self.armor,
            values=self.armors,
            state="readonly"
        )
        armor_entry.grid(row=5, column=1, sticky="EW")

        # --- Weapon ---
        weapon_label = ttk.Label(
            container,
            text="Weapon"
        )
        weapon_label.grid(row=6, column=0, sticky="EW")

        self.weapon_entry = tk.Listbox(
            container,
            listvariable=self.weapon,
            selectmode="extended",
            exportselection=False,
            selectbackground="#2CCC5B",
            highlightcolor="#1DE557",
            font=self.font,
            width=1,
            height=5
        )
        self.weapon_entry.grid(row=6, column=1, sticky="EW")

        self.weapon_entry.select_set(0)

        weapon_scrollbar = ttk.Scrollbar(container, orient="vertical")
        weapon_scrollbar.config(command=self.weapon_entry.yview)
        weapon_scrollbar.grid(row=6, column=2, sticky="NS")

        self.weapon_entry.config(yscrollcommand=weapon_scrollbar.set)

        # --- Physical Ability ---
        physical_ability_label = ttk.Label(
            container,
            text="Physical Ab."
        )
        physical_ability_label.grid(row=7, column=0, sticky="EW")

        physical_ability_entry = ttk.Entry(
            container,
            textvariable=self.physical_ability
        )
        physical_ability_entry.grid(row=7, column=1, sticky="EW")

        # --- Title ---
        title_label = ttk.Label(
            container,
            text="Title"
        )
        title_label.grid(row=8, column=0, sticky="EW")

        self.title_entry = tk.Listbox(
            container,
            listvariable=self.title,
            selectmode="extended",
            exportselection=False,
            selectbackground="#2CCC5B",
            highlightcolor="#1DE557",
            font=self.font,
            width=1,
            height=5
        )
        self.title_entry.grid(row=8, column=1, sticky="EW")
        self.title_entry.select_set(0)

        title_scrollbar = ttk.Scrollbar(container, orient="vertical")
        title_scrollbar.config(command=self.title_entry.yview)
        title_scrollbar.grid(row=8, column=2, sticky="NS")

        self.title_entry.config(yscrollcommand=title_scrollbar.set)

        # --- Ability ---
        ability_label = ttk.Label(
            container,
            text="Ability"
        )
        ability_label.grid(row=9, column=0, sticky="EW")

        self.ability_entry = tk.Listbox(
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
        self.ability_entry.grid(row=9, column=1, sticky="EW")

        self.ability_entry.select_set(0)

        ability_scrollbar = ttk.Scrollbar(container, orient="vertical")
        ability_scrollbar.config(command=self.ability_entry.yview)
        ability_scrollbar.grid(row=9, column=2, sticky="NS")

        self.ability_entry.config(yscrollcommand=ability_scrollbar.set)

        # --- Proficiency ---
        proficiency_label = ttk.Label(
            container,
            text="Proficiency"
        )
        proficiency_label.grid(row=10, column=0, sticky="EW")

        self.proficiency_entry = tk.Listbox(
            container,
            listvariable=self.proficiency,
            selectmode="extended",
            exportselection=False,
            selectbackground="#2CCC5B",
            highlightcolor="#1DE557",
            font=self.font,
            width=1,
            height=5
        )
        self.proficiency_entry.grid(row=10, column=1, sticky="EW")

        self.proficiency_entry.select_set(0)

        proficiency_scrollbar = ttk.Scrollbar(container, orient="vertical")
        proficiency_scrollbar.config(command=self.proficiency_entry.yview)
        proficiency_scrollbar.grid(row=10, column=2, sticky="NS")

        self.proficiency_entry.config(yscrollcommand=proficiency_scrollbar.set)

        # --- Description ---
        description_label = ttk.Label(
            container,
            text="Description"
        )
        description_label.grid(row=11, column=0, sticky="EW")

        self.description_entry = tk.Text(
            container,
            width=1,
            height=5
        )
        self.description_entry.grid(row=11, column=1, sticky="EW")

        description_scroll = ttk.Scrollbar(
            container,
            orient="vertical",
            command=self.description_entry.yview
        )
        description_scroll.grid(row=11, column=2, sticky="ns")

        self.description_entry["yscrollcommand"] = description_scroll.set

        self.description_entry.insert(tk.END, 'None')
