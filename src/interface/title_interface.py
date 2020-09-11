from tkinter import ttk

from src.title.title import Title


class TitleInterface(ttk.Frame):
    def __init__(self, container, entity, type_, show_search, show_home, show_edit):
        super().__init__(container)

        self.id = entity['id']
        self.name = entity['name']
        self.requirements = entity['requirements']
        self.description = entity['description']

        self.title = Title(self.name, self.requirements, self.description)

        self.create_widgets()

        self.create_buttons(show_search, show_home)

    def create_widgets(self):
        # --- Title ---

        name = ttk.Label(
            self,
            text=self.name
        )
        name.grid(row=0, column=0, sticky="EW")

        name_separator = ttk.Separator(
            self
        )
        name_separator.grid(row=1, column=0, columnspan=1, sticky="EW")

        # --- Requirements ---

        requirements = ttk.Label(
            self,
            text=f'Requirements:  {self.requirements}'
        )
        requirements.grid(row=2, column=0, sticky="EW")

        # --- Description ---

        description = ttk.Label(
            self,
            text=f'Description:  {self.description}'
        )
        description.grid(row=3, column=0, sticky="EW")

        def reconfigure_labels(event):
            requirements.configure(wraplength=self.winfo_width() - 25)
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
