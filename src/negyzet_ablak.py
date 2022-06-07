from multiprocessing.pool import TERMINATE
from tkinter import *
from mode import Mode
from Window import Window

class NegyzetAblak(Window):

    POINTS = [25, 25, 25, 150, 150, 150, 150, 25]

    def __init__(self, tk, mode: Mode):
        self.title = f"Négyzet ({mode})"
        super().__init__(tk, mode)
        
    def define_fields(self):
        self.fields = {
            "a": (Label(self.field_frame, text = "A: "), Entry(self.field_frame)),
        }

    def calc_K(self):
        if self.calc_is_error(["a"]): return

        a = self.get_field_value("a")

        return 4*a

    def calc_T(self):
        if self.calc_is_error(["a"]): return

        a = self.get_field_value("a")

        return a*a
