from multiprocessing.pool import TERMINATE
from tkinter import *
from tkinter import messagebox
from mode import Mode
from Window import Window

class TrapezAblak(Window):

    POINTS = [50, 25, 25, 100, 150, 100, 125, 25]

    def __init__(self, tk, mode: Mode):
        self.title = f"Trapéz ({mode})"
        super().__init__(tk, mode)
        
    def define_fields(self):
        self.fields = {
            "a": (Label(self.field_frame, text = "A: "), Entry(self.field_frame)),
            "b": (Label(self.field_frame, text = "B: "), Entry(self.field_frame)),
            "c": (Label(self.field_frame, text = "C: "), Entry(self.field_frame)),
            "d": (Label(self.field_frame, text = "D: "), Entry(self.field_frame)),
            "m": (Label(self.field_frame, text = "Magassag: "), Entry(self.field_frame)),
        }

    def on_init_K(self):
        self.disable_fields(["m"])

    def on_init_T(self):
        self.disable_fields(["b", "d"])

    def calc_K(self):
        if self.calc_is_error(["a", "b", "c", "d"]): return

        a = self.get_field_value("a")
        b = self.get_field_value("b")
        c = self.get_field_value("c")
        d = self.get_field_value("d")

        return a + b + c + d

    def calc_T(self):
        if self.calc_is_error(["a", "c", "m"]): return

        a = self.get_field_value("a")
        c = self.get_field_value("c")
        m = self.get_field_value("m")

        return ((a+c)/2)*m
