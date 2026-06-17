import tkinter as tk

from typing import Dict, Callable, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from ....backend import CalculatorBackEnd

class KeyBoardManagerMixin:
    """
    Calculator Mixin-class KeyBoard - manager
    """
    root:           tk.Tk
    calculator:     'CalculatorBackEnd'

    def bind_keyboard(self):
        self.root.bind("<Key>", self.on_key_press)
        self.root.bind_all("<ButtonRelease>", lambda e: self.refresh_display())        

    def on_key_press(self, event: tk.Event):

        if event.keysym in self.keyboard_shortcuts:
            func = self.keyboard_shortcuts[event.keysym]
            func()

        else:
            print(f'unsuported key for now: keysym: {event.keysym}, char: {event.char}')
            self.calculator.append_input(event.char)


            # elif event.keysym in ['Shift_L', 'Shift_R']:
            #     pass

            # elif event.keysym in ['parenleft', 'parenright']:
            #     if not self.calculator.bracket_opened:
            #         self.calculator._add_brackets('open')
            #     else:
            #         self.calculator._add_brackets('close')

            # else:
            #     key = event.char
            #     self.calculator.add_free_text(key)
      

        self.refresh_display()

    def refresh_display(self, cursor: bool = False) -> None:
        raise NotImplementedError
    
    def _setup_keyboard_shortcuts(self):
        self.keyboard_shortcuts: Dict[str, Callable[[], Any]] = {
            # system - shortcuts
            'Return'    : self.calculator.ans,              # ans
            'Control_L' : self.calculator.reset_memory,     # control -> clear
            'Control_R' : self.calculator.reset_memory,     # control -> clear
            'Delete'    : self.calculator.delete,
            'BackSpace' : self.calculator.backspace,
            'Left'      : lambda val = "<": self.calculator.resolve_system_input(val),
            'Right'     : lambda val = ">": self.calculator.resolve_system_input(val),           
        }        