from multiprocessing.pool import TERMINATE
from tkinter import *
from tkinter import messagebox
from mode import Mode

class Window:

    _EREDMENY_TEXT = "Eredmeny: {}"
    POINTS = [0, 150, 75, 0, 150, 150] # Default points
    title = "Window"

    def get_field_value(self, key):
        # This method is only used after checking if safe calculation is possible
        return int(self.fields[key][1].get())


    def place_all(self):
        self.calc_button.grid(row = len(self.fields), column = 1, sticky=E)

        self.geometry_frame.grid(row = 0, column = 0)
        self.field_frame.grid(row = 0, column = 0)
        self.canv.grid(row = 0, column = 1, padx = 20, pady = 20)

        self.result_label.grid(row = 1, column = 0, columnspan = 2, sticky=W)

        self.tl.configure(padx = 10, pady = 10)

        for i, vals in enumerate(self.fields.values()):
            vals[0].grid(row = i, column = 0)

        for i, vals in enumerate(self.fields.values()):
            vals[1].grid(row = i, column = 1)

    def on_init_K(self):
        pass

    def on_init_T(self):
        pass

    def calc_K(self):
        raise NotImplementedError

    def calc_T(self):
        raise NotImplementedError

    def disable_fields(self, fields: list):
        for field in self.fields:
            if field not in fields: continue

            self.fields[field][1].config(state="disabled")

    def calc_is_error(self, needed_fields: list):
        nums = []

        try:
            for key in self.fields:
                if key not in needed_fields: continue

                nums.append(int(self.fields[key][1].get()))
        except ValueError:
            messagebox.showerror("Hiba", "Számokat adj meg!")
            return True

        for num in nums:
            if num <= 0:
                messagebox.showerror("Hiba", "A szamok amiket megadtal ellent mondanak a fizika torvenyeinek!")
                return True

        return False

    def calc(self):
        
        # Calculating -{{
        result = 0
        if self.mode == Mode.KERULET:
            result = self.calc_K()
        elif self.mode == Mode.TERULET:
            result = self.calc_T()
        result = str(round(result, 2))

        # }}
        
        self.result_label.config(text=self._EREDMENY_TEXT.format(result))

    def define_fields(self):
        self.fields = {
            "a": (Label(self.field_frame, text = "A: "), Entry(self.field_frame)),
            "b": (Label(self.field_frame, text = "B: "), Entry(self.field_frame)),
            "c": (Label(self.field_frame, text = "C: "), Entry(self.field_frame)),
        }

    def __init__(self, tk, mode: Mode) -> None:

        self.mode = mode
        self.tl = Toplevel(tk)
        self.tl.title(self.title)
        self.tl.resizable(False, False) 
        self.geometry_frame = Frame(self.tl)
        self.field_frame = Frame(self.geometry_frame)

        self.define_fields()

        self.canv = Canvas(self.geometry_frame, width = 150, height = 150)
        self.canv.create_polygon(self.POINTS, fill = "white", outline = "black")

        self.calc_button = Button(self.field_frame, text="Szamitas", command=self.calc)
        self.result_label = Label(self.tl, text = self._EREDMENY_TEXT.format(""))

        self.place_all()
        
        if mode == Mode.KERULET:
            self.on_init_K()
        elif mode == Mode.TERULET:
            self.on_init_T()

        self.tl.mainloop()
