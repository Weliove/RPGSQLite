import re
import tkinter as tk
from tkinter import ttk
import tkinter.font as font

from src import Home
from src import CreateAvatar
from src.interface.interface import Interface
from src.search.search import Search


class RPG(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("RPG - Home")

        self.resizable(False, False)

        self.frames = dict()

        # --- Create Frames ---
        self.home_frame = Home(
            self,
            lambda: self.show_create_avatar()
        )
        self.home_frame.grid(row=0, column=0, sticky="NSEW")

        self.search_frame = Search(self, [], '', lambda: self.show_frame(Home))

        self.create_avatar_frame = CreateAvatar(self, lambda: self.show_frame(Home))

        self.interface_frame = None

        self.frames[Home] = self.home_frame
        self.frames[CreateAvatar] = self.create_avatar_frame
        self.frames[Search] = self.search_frame
        self.frames[Interface] = self.interface_frame

        # --- Show Frame ---
        self.show_frame(Home)

    def show_frame(self, container):
        local_title = " "
        local_title_array = re.findall('[A-Z][^A-Z]*', str(container.__name__))
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

    def show_interface(self, entity, type_):
        self.check_frame_existence(self.interface_frame)

        self.interface_frame = Interface(self, entity, type_, lambda: self.show_frame(Home))
        self.interface_frame.grid(row=0, column=0, sticky="NSEW")

        self.frames[Interface] = self.interface_frame
        self.show_frame(Interface)

    def check_frame_existence(self, frame):
        if frame is not None and frame.winfo_exists():
            frame.destroy()


root = RPG()

style = ttk.Style(root)
style.theme_use("clam")

font.nametofont("TkDefaultFont").configure(size=12)

root.mainloop()
