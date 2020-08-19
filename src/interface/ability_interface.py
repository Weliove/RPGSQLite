from tkinter import ttk

from src.ability.ability import Ability


class AbilityInterface(ttk.Frame):
    def __init__(self, container, entity, type_, show_search, show_home, show_interface_verification):
        super().__init__(container)

        print(f'Abilities: {entity}')

        self.abilities_type = {1: 'Character Ability', 2: 'NPC Ability', 3: 'Monster Ability', 4: 'Item Ability'}

        self.id = entity['id']
        self.name = entity['name']
        self.type = entity['type']
        self.casting = entity['casting']
        self.components = entity['components']
        self.requirements = entity['requirements']
        self.conditions = entity['conditions']
        self.effects = entity['effects']
        self.description = entity['description']

        self.ability = Ability(self.name, self.name, self.type, self.casting, self.components, self.requirements,
                               self.conditions, self.effects, self.description)

        self.create_widgets()

        self.create_buttons(show_search, show_home)

    def create_widgets(self):
        # --- Item ---

        name = ttk.Label(
            self,
            text=self.name
        )
        name.grid(row=0, column=0, sticky="EW")

        name_separator = ttk.Separator(
            self
        )
        name_separator.grid(row=1, column=0, columnspan=1, sticky="EW")

        # --- Type ---

        type_ = ttk.Label(
            self,
            text='Type:  ' + self.abilities_type[self.type]
        )
        type_.grid(row=2, column=0, sticky="EW")

        # --- Casting ---

        casting = ttk.Label(
            self,
            text='Casting:  ' + self.casting
        )
        casting.grid(row=3, column=0, sticky="EW")

        # --- Components ---

        components = ttk.Label(
            self,
            text='Components:  ' + self.components
        )
        components.grid(row=4, column=0, sticky="EW")

        # --- Requirements ---

        requirements = ttk.Label(
            self,
            text='Requirements:  ' + self.requirements
        )
        requirements.grid(row=5, column=0, sticky="EW")

        # --- Conditions ---

        conditions = ttk.Label(
            self,
            text='Conditions:  ' + self.conditions
        )
        conditions.grid(row=6, column=0, sticky="EW")

        # --- Effects ---

        effects = ttk.Label(
            self,
            text='Effects:  ' + self.effects
        )
        effects.grid(row=7, column=0, sticky="EW")

        # --- Description ---

        description = ttk.Label(
            self,
            text='Description:  ' + self.description
        )
        description.grid(row=8, column=0, sticky="EW")

        def reconfigure_labels(event):
            casting.configure(wraplength=self.winfo_width() - 25)
            components.configure(wraplength=self.winfo_width() - 25)
            requirements.configure(wraplength=self.winfo_width() - 25)
            conditions.configure(wraplength=self.winfo_width() - 25)
            effects.configure(wraplength=self.winfo_width() - 25)
            description.configure(wraplength=self.winfo_width() - 25)

        self.bind("<Configure>", reconfigure_labels)

    def create_buttons(self, show_search, show_home):
        back_button = ttk.Button(
            self,
            text="← Back",
            command=show_search,
            cursor="hand2"
        )
        back_button.grid(column=0, sticky="EW")

        home_button = ttk.Button(
            self,
            text="Home",
            command=show_home,
            cursor="hand2"
        )
        home_button.grid(column=0, sticky="EW")
