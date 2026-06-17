import tkinter as tk
# from tkinter import ttk

from .configmanager import ConfigManagerMixin 
from .geometrymanager import GeometryManagerMixin
from .makeupmanager import MakeupManagerMixin
from .buttons import ButtonGridManagerMixin
from .keyboard import KeyBoardManagerMixin

from ...backend import PathManager, CalculatorBackEnd


class Calculator(ConfigManagerMixin,
                 GeometryManagerMixin, 
                 MakeupManagerMixin, 
                 ButtonGridManagerMixin, 
                 KeyBoardManagerMixin):

    """
    Main calculator logic
    """

    def __init__(self):
        self.root       = tk.Tk()
        self.calculator = CalculatorBackEnd()

        self.pathmanager = PathManager()

        self.set_config()
        self.set_geometry()
        self.set_outlook()
        self.set_grid()
        self.bind_keyboard()
        self._setup_keyboard_shortcuts()

        self.cursor_idx      = 0
        self._cursor_visible = False   # is the cursor drawn right now?
        self._cursor_job     = None    # handle to the pending after() call        

    def run(self):
        self.start_cursor_blink()
        self.root.mainloop()

    def refresh_display(self, cursor: bool = False):
        
        display_expr = self.calculator.get_display_expression(cursor)
        outcome_expr = self.calculator.result

        self.expression_var.set(display_expr)

        self.result_var.set(outcome_expr)

    def start_cursor_blink(self):
        if self._cursor_job is not None:
            self.root.after_cancel(self._cursor_job)

        self._cursor_visible = True
        self.refresh_display(cursor=self._cursor_visible)
        self._cursor_job = self.root.after(500, self._blink)

    def _blink(self):
        self._cursor_visible = not self._cursor_visible
        self.refresh_display(cursor=self._cursor_visible)
        self._cursor_job = self.root.after(500, self._blink)
        
    def stop_cursor_blink(self):
        if self._cursor_job is not None:
            self.root.after_cancel(self._cursor_job)
            self._cursor_job = None
        self._cursor_visible = False            