from multiprocessing.pool import TERMINATE
from tkinter import *
from tkinter import messagebox
from mode import Mode

EREDMENY_TEXT = "Eredmeny: {}"
POINTS = [0, 150, 75, 0, 150, 150]

class TesztAblak:

    def place_all(self):
        self.calc_button.grid(row = 3, column = 1, sticky=E)

        self.geometry_frame.grid(row = 0, column = 0)
        self.field_frame.grid(row = 0, column = 0)
        self.canv.grid(row = 0, column = 1, padx = 20, pady = 20)

        self.result_label.grid(row = 1, column = 0, columnspan = 2, sticky=W)

        self.tl.configure(padx = 10, pady = 10)

        for i, vals in enumerate(self.fields.values()):
            vals[0].grid(row = i, column = 0)

        for i, vals in enumerate(self.fields.values()):
            vals[1].grid(row = i, column = 1)


    def calc(self):

        try:
            a = int(self.fields["a"][1].get())
            b = int(self.fields["b"][1].get())
            c = int(self.fields["c"][1].get())
        except ValueError:
            messagebox.showerror("Hiba", "Számokat adj meg!")
            return

        if a <= 0 or b <= 0 or c <= 0:
            return messagebox.showerror("Hiba", "A szamok amiket megadtal ellent mondanak a fizika torvenyeinek!")
        # }}
        
        # Calculating -{{
        result = 0
        if self.mode == Mode.KERULET:
            result = a + b + c
        elif self.mode == Mode.TERULET:
            result = a * b * c
        result = str(result)

        # }}
        
        self.result_label.config(text=EREDMENY_TEXT.format(result))

    def __init__(self, tk, mode: Mode) -> None:

        self.mode = mode
        self.tl = Toplevel(tk)
        self.tl.title("Teszt")
        self.geometry_frame = Frame(self.tl)
        self.field_frame = Frame(self.geometry_frame)

        self.fields = {
            "a": (Label(self.field_frame, text = "A: "), Entry(self.field_frame)),
            "b": (Label(self.field_frame, text = "B: "), Entry(self.field_frame)),
            "c": (Label(self.field_frame, text = "C: "), Entry(self.field_frame)),
        }

        self.canv = Canvas(self.geometry_frame, width = 150, height = 150)
        self.canv.create_polygon(POINTS, fill = "white", outline = "black")

        self.calc_button = Button(self.field_frame, text="Szamitas", command=self.calc)
        self.result_label = Label(self.tl, text = EREDMENY_TEXT.format(""))

        self.place_all()
        self.tl.mainloop()
