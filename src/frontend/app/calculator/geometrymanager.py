import tkinter as tk

class GeometryManagerMixin:
    """
    Calculator Mixin-class Geometry - manager
    uses attributes set by CalculatorConfigMixin
    """

    root:           tk.Tk
    window_height:  int 
    window_width:   int

    def set_geometry(self):
        screen_width    = self.root.winfo_screenwidth()
        screen_height   = self.root.winfo_screenheight()

        # find the center point
        center_x = screen_width - self.window_width - 10
        center_y = int(screen_height/2 - self.window_height / 2)

        # set the position of the window to the center of the screen
        self.root.geometry(f'{self.window_width}x{self.window_height}+{center_x}+{center_y}')    

        self.root.resizable(False, False)