from tkinter import ttk

from src.connection.database import search_database
from src.connection.handle_users import get_user_items, get_user_abilities, get_user_titles, get_user_proficiencies
from src.edit.edit_ability import EditAbility
from src.edit.edit_item import EditItem
from src.edit.edit_proficiency import EditProficiency
from src.edit.edit_title import EditTitle
from src.edit.edit_user import EditUser


class EditWidget(ttk.Frame):
    def __init__(self, parent, container, entity, entity_type, parent_name, parent_type, show_interface,
                 search_entities_name, search_type, show_interface_verification, interface_verification_dict,
                 show_home):
        super().__init__(container)

        self.parent = parent

        self.entity = entity
        self.entity_type = entity_type
        self.parent_name = parent_name
        self.parent_type = parent_type
        self.show_interface = show_interface
        self.search_entities_name = search_entities_name
        self.search_type = search_type
        self.show_interface_verification = show_interface_verification
        self.interface_verification_dict = interface_verification_dict
        self.show_home = show_home

        self.type = search_database[entity_type]

        self.edit_widget_frame = None

        self.create_frame(entity, show_interface)

        self.create_buttons()

    def create_frame(self, entity, show_interface):
        self.check_frame_existence(self.edit_widget_frame)

        if self.type == 'users':
            self.edit_widget_frame = EditUser(self, entity, self.search_entities_name, self.search_type, show_interface)
        elif self.type == 'items':
            self.edit_widget_frame = EditItem(self, entity, self.search_entities_name, self.search_type, show_interface,
                                              self.show_interface_verification, self.interface_verification_dict)
        elif self.type == 'abilities':
            self.edit_widget_frame = EditAbility(self, entity, self.search_entities_name, self.search_type,
                                                 show_interface, self.show_interface_verification,
                                                 self.interface_verification_dict)
        elif self.type == 'titles':
            self.edit_widget_frame = EditTitle(self, entity, self.search_entities_name, self.search_type,
                                               show_interface, self.show_interface_verification,
                                               self.interface_verification_dict)
        elif self.type == 'proficiencies':
            self.edit_widget_frame = EditProficiency(self, entity, self.search_entities_name, self.search_type,
                                                     show_interface, self.show_interface_verification,
                                                     self.interface_verification_dict)

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
            command=self.save,
            cursor='hand2'
        )
        save_button.grid(row=1, column=0)

        back_button = ttk.Button(
            buttons_frame,
            text='← Back',
            command=self.back,
            cursor='hand2'
        )
        back_button.grid(row=2, column=0)

        for child in buttons_frame.winfo_children():
            child.grid_configure(padx=5, pady=5, sticky="EW")

    def save(self):
        if self.type == 'users':
            proficiency = self.edit_widget_frame.set_proficiencies()

            if proficiency is not None:
                self.parent.container.parent.show_proficiencies_level(
                    proficiency['proficiency'],
                    proficiency['proficiency_result'],
                    proficiency['self']
                )
            else:
                self.edit_widget_frame.edit_entity()
        else:
            self.edit_widget_frame.edit_entity()

    def back(self):
        if self.parent_name is not None and self.interface_verification_dict is not None:
            entities = None
            user_name = self.interface_verification_dict['name']
            user_type = self.interface_verification_dict['type']
            entity_type = self.interface_verification_dict['entity_type']

            if entity_type == 'Item':
                entities = get_user_items(user_name)
            elif entity_type == 'Ability':
                entities = get_user_abilities(user_name)
            elif entity_type == 'Title':
                entities = get_user_titles(user_name)
            elif entity_type == 'Proficiency':
                entities = get_user_proficiencies(user_name)

            self.show_interface_verification(entities, entity_type, user_name, user_type, self.search_entities_name,
                                             self.search_type)
        else:
            self.show_interface(self.entity, self.entity_type, self.search_entities_name, self.search_type)

    def check_frame_existence(self, frame):
        if frame is not None and frame.winfo_exists():
            frame.destroy()
