from multiprocessing.pool import TERMINATE
from tkinter import *
from mode import Mode
from Window import Window

class KorAblak(Window):

    POINTS = [0, 0]

    def __init__(self, tk, mode: Mode):
        self.title = f"Kör ({mode})"
        super().__init__(tk, mode)
        
    def define_fields(self):
        self.fields = {
            "r": (Label(self.field_frame, text = "r: "), Entry(self.field_frame)),
        }

    def calc_K(self):
        if self.calc_is_error(["r"]): return

        r = self.get_field_value("r")

        return 2*r*3.14

    def calc_T(self):
        if self.calc_is_error(["r"]): return

        r = self.get_field_value("r")
 
        return r*r*3.14
