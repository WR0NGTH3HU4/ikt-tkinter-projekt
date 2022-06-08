from cmath import e
from multiprocessing.pool import TERMINATE
from tkinter import *
from mode import Mode
from Window import Window

class DeltoidAblak(Window):

    POINTS = [0,0]

    def __init__(self, tk, mode: Mode):
        self.title = f"Deltoid ({mode})"
        super().__init__(tk, mode)
        
    def define_fields(self):
        self.fields = {
            "a": (Label(self.field_frame, text = "A: "), Entry(self.field_frame)),
            "b": (Label(self.field_frame, text = "B: "), Entry(self.field_frame)),
            "e": (Label(self.field_frame, text = "C: "), Entry(self.field_frame)),
            "f": (Label(self.field_frame, text = "F: "), Entry(self.field_frame)),
        }

    def on_init_K(self):
        self.disable_fields(["e", "f"])
    
    def on_init_T(self):
        self.disable_fields(["a", "b"])

    def calc_K(self):
        if self.calc_is_error(["a", "b"]): return

        a = self.get_field_value("a")
        b = self.get_field_value("b")

        return 2*(a+b)

    def calc_T(self):
        if self.calc_is_error(["e", "f"]): return

        a = self.get_field_value("e")
        m = self.get_field_value("f")

        return (e* f )/2
