from multiprocessing.pool import TERMINATE
from tkinter import *
from mode import Mode
from Window import Window

class RombuszAblak(Window):

    POINTS = [55, 25, 30, 100, 120, 100, 145, 25]

    def __init__(self, tk, mode: Mode):
        self.title = f"Rombusz ({mode})"
        super().__init__(tk, mode)
        
    def define_fields(self):
        self.fields = {
            "a": (Label(self.field_frame, text = "A: "), Entry(self.field_frame)),
            "m": (Label(self.field_frame, text = "Magassag: "), Entry(self.field_frame)),
        }

    def on_init_K(self):
        self.disable_fields(["m"])

    def calc_K(self):
        if self.calc_is_error(["a"]): return

        a = self.get_field_value("a")

        return 4*a

    def calc_T(self):
        if self.calc_is_error(["a", "m"]): return

        a = self.get_field_value("a")
        m = self.get_field_value("m")

        return a*m
