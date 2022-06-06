from multiprocessing.pool import TERMINATE
from tkinter import *
from mode import Mode
from Window import Window

class TeglalapAblak(Window):

    POINTS = [25, 25, 25, 100, 150, 100, 150, 25]

    def __init__(self, tk, mode: Mode):
        self.title = f"Téglalap ({mode})"
        super().__init__(tk, mode)
        
    def define_fields(self):
        self.fields = {
            "a": (Label(self.field_frame, text = "A: "), Entry(self.field_frame)),
            "b": (Label(self.field_frame, text = "B: "), Entry(self.field_frame)),
        }

    def calc_K(self):
        if self.calc_is_error(["a", "b"]): return

        a = self.get_field_value("a")
        b = self.get_field_value("b")

        return 2*(a + b)

    def calc_T(self):
        if self.calc_is_error(["a", "b"]): return

        a = self.get_field_value("a")
        b = self.get_field_value("b")

        return a*b
