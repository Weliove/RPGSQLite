from tkinter import ttk

from src.connection.database import search_database


class WikiEditWidget(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.edit_widget_frame = None

        # self.create_frame(entity, entity_type, show_interface)

        self.create_buttons()

    def create_frame(self, entity, entity_type, show_interface):
        self.check_frame_existence(self.edit_widget_frame)

        print(entity_type)
        type_ = search_database[entity_type]

        if type_ == 'users':
            self.edit_widget_frame = EditUser(self, entity, show_interface)
        elif type_ == 'items':
            self.edit_widget_frame = EditItem(self, entity, show_interface)
        elif type_ == 'abilities':
            self.edit_widget_frame = EditAbility(self, entity, show_interface)
        elif type_ == 'titles':
            self.edit_widget_frame = EditTitle(self, entity, show_interface)

        self.edit_widget_frame.grid(row=0, column=0, sticky="NSEW")
        self.edit_widget_frame.columnconfigure(0, weight=1)

        for child in self.edit_widget_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def create_buttons(self):
        buttons_frame = ttk.Frame(self)
        buttons_frame.grid(row=1, column=0, sticky="EW")
        buttons_frame.columnconfigure(0, weight=1)

        separator = ttk.Separator(
            buttons_frame
        )
        separator.grid(row=0, column=0, columnspan=1)

        save_button = ttk.Button(
            buttons_frame,
            text='Save',
            command=self.edit_widget_frame.edit_entity,
            cursor='hand2'
        )
        save_button.grid(row=1, column=0)

        back_button = ttk.Button(
            buttons_frame,
            text='← Back',
            command=lambda: self.show_interface(self.entity, self.entity_type),
            cursor='hand2'
        )
        back_button.grid(row=2, column=0)

        for child in buttons_frame.winfo_children():
            child.grid_configure(padx=5, pady=5, sticky="EW")

    def check_frame_existence(self, frame):
        if frame is not None and frame.winfo_exists():
            frame.destroy()
