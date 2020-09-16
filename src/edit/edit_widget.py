from tkinter import ttk

from src.edit.edit_item import EditItem
from src.edit.edit_title import EditTitle
from src.edit.edit_user import EditUser


class EditWidget(ttk.Frame):
    def __init__(self, container, entity, entity_type, show_interface, show_home):
        super().__init__(container)

        self.entity = entity
        self.entity_type = entity_type
        self.show_interface = show_interface
        self.show_home = show_home

        self.edit_widget_frame = None

        self.create_frame(entity, entity_type, show_interface)

        self.create_buttons()

    def create_frame(self, entity, entity_type, show_interface):
        self.check_frame_existence(self.edit_widget_frame)

        print(entity_type)

        if entity_type == 'users':
            self.edit_widget_frame = EditUser(self, entity, show_interface)
        elif entity_type == 'items':
            self.edit_widget_frame = EditItem(self, entity, show_interface)
        elif entity_type == 'abilities':
            pass
        elif entity_type == 'titles':
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
