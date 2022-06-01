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

    def calc_K(self):
        return 69

    def calc_T(self):
        return 3452
