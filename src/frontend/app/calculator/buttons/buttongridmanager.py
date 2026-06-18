from typing import List, TYPE_CHECKING
import tkinter as tk
from .buttongrids import GRID1, GRID2, ButtonGrid

if TYPE_CHECKING:
    from .....backend import CalculatorBackEnd


class ButtonGridManagerMixin:
    """
    Screens:
        - top: display
        - nav: navigation bars
        - bottom: grid (n = 2)
    """

    root:           tk.Tk
    calculator:     'CalculatorBackEnd'
    window_height:  int 
    window_width:   int
    cursor_idx:     int

    def set_grid(self):
        # initialize screens
        self.screens:    List[tk.Frame] = self._divide_screen() 
        self._init_top_frame(self.screens[0])
        self._init_nav_frame(self.screens[1])

        # init grids
        self.grid_pages: List[tk.Frame] = self._init_grids(self.screens[-1])

        self._fill_grid(GRID1, 0)       
        self._fill_grid(GRID2, 1)               

        self.show_grid(0)

    def _divide_screen(self) -> List[tk.Frame]:
        top     = tk.Frame(self.root, bg="white", bd=5, relief="solid")
        nav     = tk.Frame(self.root, bg="white", bd=5, relief="solid", height=40)
        bottom  = tk.Frame(self.root, bg="white", bd=5, relief="solid")

        top.pack(fill="both", expand=True)

        nav.pack(fill="x")
        nav.pack_propagate(False)

        bottom.pack(fill="both", expand=True)

        return [top, nav, bottom]
    
    def _init_top_frame(self, frame: tk.Frame):
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(2, weight=1)
        frame.columnconfigure(0, weight=1)

        self.expression_var = tk.StringVar(value=self.calculator.expression_str)
        self.result_var     = tk.StringVar(value=self.calculator.result)

        tk.Label(
            frame,
            textvariable=self.expression_var,
            bg="white", fg="black",
            anchor="w",
            font=("Courier", 16)
        ).grid(row=0, column=0, sticky="nsew", padx=8, pady=(8, 2))

        tk.Label(
            frame,
            textvariable=self.result_var,
            bg="white", fg="gray40",
            anchor="e",
            font=("Courier", 22, "bold")
        ).grid(row=1, column=0, sticky="nsew", padx=8, pady=(2, 8))

    def _init_nav_frame(self, frame: tk.Frame):
        frame.columnconfigure((0, 1), weight=1)

        tk.Button(
            frame,
            text="Basic",
            command=lambda: self.show_grid(0)
        ).grid(row=0, column=0, sticky="nsew")

        tk.Button(
            frame,
            text="Func",
            command=lambda: self.show_grid(1)
        ).grid(row=0, column=1, sticky="nsew")      
        
    def _init_grids(self, frame: tk.Frame) -> List[tk.Frame]:
        pages: List[tk.Frame] = []
        
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)

        for _ in range(2):
            page = tk.Frame(frame, bg="white")
            page.grid(row=0, column=0, sticky="nsew")

            # important
            page.rowconfigure((0,1,2,3), weight=1)
            page.columnconfigure((0,1,2,3), weight=1)
            pages.append(page)  
        return pages        

    def _fill_grid(self, GRID: ButtonGrid, idx: int):
        frame: tk.Frame = self.grid_pages[idx]
        for row in range(GRID.nrow):
            frame.rowconfigure(row, weight=1)

        for col in range(GRID.ncol):
            frame.columnconfigure(col, weight=1)

        for row, button_row in enumerate(GRID):

            for col, button in enumerate(button_row):

                if button.type == 'input':
                    func = lambda val = button.representation: self.calculator.append_input(val) # type: ignore

                elif button.type == 'notimplemented':
                    func = lambda val = button.value: print(f'button with value {val} has not been implemented')

                elif button.type == 'system':
                    func = lambda val = button.value: self.calculator.resolve_system_input(val)
                
                else:
                    raise ValueError(f'unknown button type {button.type}')

                btn = tk.Button(
                    frame,
                    text    = button.label,
                    command = func,
                    **button.appearance
                )

                btn.grid(
                    row=row,
                    column=button.col if button.col else col ,
                    columnspan=button.span,
                    sticky="nsew",
                    padx=2,
                    pady=2
                )

    def show_grid(self, index: int):
        self.grid_pages[index].tkraise() # type: ignore                

        
