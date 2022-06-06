from multiprocessing.pool import TERMINATE
from tkinter import *
from tkinter import messagebox
from mode import Mode
from Window import Window

class ParalelogrammaAblak(Window):

    POINTS = [25, 25, 0, 100, 125, 100, 150, 25]

    def __init__(self, tk, mode: Mode):
        self.title = f"Paralelogramma ({mode})"
        super().__init__(tk, mode)
        
    def define_fields(self):
        self.fields = {
            "a": (Label(self.field_frame, text = "A: "), Entry(self.field_frame)),
            "b": (Label(self.field_frame, text = "B: "), Entry(self.field_frame)),
            "m": (Label(self.field_frame, text = "Magassag: "), Entry(self.field_frame)),
        }

    def on_init_K(self):
        self.disable_fields(["m"])

    def on_init_T(self):
        self.disable_fields(["b"])

    def calc_K(self):
        if self.calc_is_error(["a", "b"]): return

        a = self.get_field_value("a")
        b = self.get_field_value("b")

        return 2*(a + b)

    def calc_T(self):
        if self.calc_is_error(["a", "m"]): return

        a = self.get_field_value("a")
        m = self.get_field_value("m")

        return a*m
