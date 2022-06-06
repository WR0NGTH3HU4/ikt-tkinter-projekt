from multiprocessing.pool import TERMINATE
from tkinter import *
from tkinter import messagebox
from mode import Mode
from Window import Window

class TesztAblak(Window):

    POINTS = [25, 25, 25, 150, 150, 150, 150, 25]

    def __init__(self, tk, mode: Mode):
        super().__init__(tk, mode)
        
    def define_fields(self):
        self.fields = {
            "a": (Label(self.field_frame, text = "A: "), Entry(self.field_frame)),
            "b": (Label(self.field_frame, text = "B: "), Entry(self.field_frame)),
        }

    def on_init_K(self):
        self.disable_fields(["a"])

    def calc_K(self):
        if self.calc_is_error(["b"]): return

        return 69

    def calc_T(self):
        if self.calc_is_error(["a", "b"]): return

        return 3452
