import re
import tkinter as tk
from tkinter import ttk
import tkinter.font as font

from src import Home
from src import CreateAvatar
from src.ability.create_ability import CreateAbility
from src.edit.edit import Edit
from src.interface.interface import Interface
from src.interface.interface_verification import InterfaceVerification
from src.item.create_item import CreateItem
from src.proficiency.create_proficiency import CreateProficiency
from src.search.search import Search
from src.title.create_title import CreateTitle
from src.wiki.create_wiki import CreateWiki


class RPG(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("RPG - Home")

        self.resizable(False, False)

        self.frames = dict()

        # --- Create Frames ---
        self.home_frame = Home(
            self,
            lambda: self.show_create_avatar(),
            lambda: self.show_create_item(),
            lambda: self.show_create_ability(),
            lambda: self.show_create_title(),
            lambda: self.show_create_proficiency(),
            lambda: self.show_wiki()
        )
        self.home_frame.grid(row=0, column=0, sticky="NSEW")

        self.search_frame = Search(self, [], '', lambda: self.show_frame(Home))

        self.create_avatar_frame = CreateAvatar(self, lambda: self.show_frame(Home))

        self.create_item_frame = CreateItem(self, lambda: self.show_frame(Home))

        self.create_ability_frame = CreateAbility(self, lambda: self.show_frame(Home))

        self.create_title_frame = CreateTitle(self, lambda: self.show_frame(Home))

        self.create_proficiency_frame = CreateProficiency(self, lambda: self.show_frame(Home))

        self.interface_frame = None

        self.edit_frame = None

        self.interface_verification_frame = None

        self.wiki_frame = CreateWiki(self, lambda: self.show_frame(Home))

        self.frames = {
            Home: self.home_frame,
            CreateAvatar: self.create_avatar_frame,
            Search: self.search_frame,
            CreateItem: self.create_item_frame,
            CreateAbility: self.create_ability_frame,
            CreateTitle: self.create_title_frame,
            CreateProficiency: self.create_proficiency_frame,
            Interface: self.interface_frame,
            Edit: self.edit_frame,
            InterfaceVerification: self.interface_verification_frame,
            CreateWiki: self.wiki_frame
        }

        # --- Show Frame ---
        self.show_frame(Home)

    def show_frame(self, container):
        local_title = " "

        if type(type):
            local_title_array = re.findall('[A-Z][^A-Z]*', str(container.__name__))
        else:
            local_title_array = re.findall('[A-Z][^A-Z]*', container)

        self.title(f"RPG - {local_title.join(local_title_array)}")

        frame = self.frames[container]
        frame.tkraise()

    def show_create_avatar(self):
        self.check_frame_existence(self.create_avatar_frame)

        self.create_avatar_frame = CreateAvatar(self, lambda: self.show_frame(Home))
        self.create_avatar_frame.grid(row=0, column=0, sticky="NSEW")

        self.frames[CreateAvatar] = self.create_avatar_frame
        self.show_frame(CreateAvatar)

    def show_search(self, entities_name, type_):
        self.check_frame_existence(self.search_frame)

        self.search_frame = Search(self, entities_name, type_, lambda: self.show_frame(Home))
        self.search_frame.grid(row=0, column=0, sticky="NSEW")

        self.frames[Search] = self.search_frame
        self.show_frame(Search)

    def show_create_item(self):
        self.check_frame_existence(self.create_item_frame)

        self.create_item_frame = CreateItem(self, lambda: self.show_frame(Home))
        self.create_item_frame.grid(row=0, column=0, sticky="NSEW")

        self.frames[CreateItem] = self.create_item_frame
        self.show_frame(CreateItem)

    def show_create_ability(self):
        self.check_frame_existence(self.create_ability_frame)

        self.create_ability_frame = CreateAbility(self, lambda: self.show_frame(Home))
        self.create_ability_frame.grid(row=0, column=0, sticky="NSEW")

        self.frames[CreateAbility] = self.create_ability_frame
        self.show_frame(CreateAbility)

    def show_create_title(self):
        self.check_frame_existence(self.create_title_frame)

        self.create_title_frame = CreateTitle(self, lambda: self.show_frame(Home))
        self.create_title_frame.grid(row=0, column=0, sticky="NSEW")

        self.frames[CreateTitle] = self.create_title_frame
        self.show_frame(CreateTitle)

    def show_create_proficiency(self):
        self.check_frame_existence(self.create_proficiency_frame)

        self.create_proficiency_frame = CreateProficiency(self, lambda: self.show_frame(Home))
        self.create_proficiency_frame.grid(row=0, column=0, sticky='NSEW')

        self.frames[CreateProficiency] = self.create_proficiency_frame
        self.show_frame(CreateProficiency)

    def show_interface(self, entity, type_):
        self.check_frame_existence(self.interface_frame)

        self.interface_frame = Interface(
            self,
            entity,
            type_,
            lambda: self.show_frame(Search),
            lambda: self.show_frame(Home),
            self.show_edit,
            self.show_interface_verification
        )
        self.interface_frame.grid(row=0, column=0, sticky="NSEW")

        self.frames[Interface] = self.interface_frame
        self.show_frame(Interface)

    def show_edit(self, entity, type_):
        self.check_frame_existence(self.edit_frame)

        self.edit_frame = Edit(self, entity, type_, self.show_interface, lambda: self.show_frame(Home))
        self.edit_frame.grid(row=0, column=0, sticky="NSEW")

        self.frames[Edit] = self.edit_frame
        self.show_frame(Edit)

    def show_interface_verification(self, entity, type_):
        self.check_frame_existence(self.interface_verification_frame)

        self.interface_verification_frame = InterfaceVerification(
            self,
            entity,
            type_,
            lambda: self.show_frame(Interface),
            lambda: self.show_frame(Home),
            self.show_edit,
            self.show_interface_verification
        )
        self.interface_verification_frame.grid(row=0, column=0, sticky="NSEW")

        self.frames[InterfaceVerification] = self.interface_verification_frame
        self.show_frame(InterfaceVerification)

    def show_wiki(self):
        self.check_frame_existence(self.wiki_frame)

        self.wiki_frame = CreateWiki(self, lambda: self.show_frame(Home))
        self.wiki_frame.grid(row=0, column=0, sticky="NSEW")

        self.frames[CreateWiki] = self.wiki_frame
        self.show_frame(CreateWiki)

    def check_frame_existence(self, frame):
        if frame is not None and frame.winfo_exists():
            frame.destroy()


root = RPG()

style = ttk.Style(root)
style.theme_use("clam")

font.nametofont("TkDefaultFont").configure(size=12)

root.mainloop()
