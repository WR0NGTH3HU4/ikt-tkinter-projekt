from multiprocessing.pool import TERMINATE
from tkinter import *
from mode import Mode
from Window import Window

class HaromszogAblak(Window):

    POINTS = [25, 125, 75, 25, 125, 125]

    def __init__(self, tk, mode: Mode):
        self.title = f"Háromszög ({mode})"
        super().__init__(tk, mode)
        
    def define_fields(self):
        self.fields = {
            "a": (Label(self.field_frame, text = "A: "), Entry(self.field_frame)),
            "b": (Label(self.field_frame, text = "B: "), Entry(self.field_frame)),
            "c": (Label(self.field_frame, text = "C: "), Entry(self.field_frame)),
            "m": (Label(self.field_frame, text = "Magassag: "), Entry(self.field_frame)),
        }

    def on_init_K(self):
        self.disable_fields(["m"])
    
    def on_init_T(self):
        self.disable_fields(["b", "c"])

    def calc_K(self):
        if self.calc_is_error(["a", "b", "c"]): return

        a = self.get_field_value("a")
        b = self.get_field_value("b")
        c = self.get_field_value("c")

        return a + b + c

    def calc_T(self):
        if self.calc_is_error(["a", "m"]): return

        a = self.get_field_value("a")
        m = self.get_field_value("m")

        return (a*m)/2
