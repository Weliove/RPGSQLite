import re
import tkinter as tk
from tkinter import ttk
import tkinter.font as font

# Add 3 combo boxes que vão relacionar a habilidade à um Avatar (Character, NPC ou Monster)
# Add botão para adicionar outras frames de habilidade


class CreateAbility(ttk.Frame):
    def __init__(self, parent, show_home):
        super().__init__(parent)
