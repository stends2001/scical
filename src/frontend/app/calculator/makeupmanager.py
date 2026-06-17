import tkinter as tk
import os
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....backend import PathManager

class MakeupManagerMixin:

    root:           tk.Tk
    title:          str
    pathmanager:    'PathManager'

    def set_makeup(self):
        self.root.title(self.title) 
        self.root.iconbitmap(os.path.join(self.pathmanager.project_root,'assets/app_icon.ico')) # type: ignore