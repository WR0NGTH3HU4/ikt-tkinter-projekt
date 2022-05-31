from multiprocessing.pool import TERMINATE
from tkinter import *
from tkinter import messagebox
from mode import Mode

EREDMENY_TEXT = "Eredmeny: {}"

def teszt_ablak(tk, mode: Mode, nev):

    def calc():

        # Error handling -{{
        try:
            a = int(a_entry.get())
            b = int(b_entry.get())
            c = int(c_entry.get())
        except ValueError:
            messagebox.showerror("Hiba", "Számokat adj meg!")
            return

        if a <= 0 or b <= 0 or c <= 0:
            return messagebox.showerror("Hiba", "A szamok amiket megadtal ellent mondanak a fizika torvenyeinek!")
        # }}
        
        # Calculating -{{
        result = 0
        if mode == Mode.KERULET:
            result = a + b + c
        elif mode == Mode.TERULET:
            result = a * b * c
        result = str(result)

        # }}
        
        result_label.config(text=EREDMENY_TEXT.format(result))

    tl = Toplevel(tk)
    tl.title(nev)

    # bal oldal
    
    geometry_frame = Frame(tl)
    field_frame = Frame(geometry_frame)

    a_label = Label(field_frame, text = "A: ")
    b_label = Label(field_frame, text = "B: ")
    c_label = Label(field_frame, text = "C: ")

    a_entry = Entry(field_frame)
    b_entry = Entry(field_frame)
    c_entry = Entry(field_frame)

    calc_button = Button(field_frame, text="Szamitas", command=calc)

    # jobb oldal

    canv = Canvas(geometry_frame, width = 150, height = 150)
    points = [0, 150, 75, 0, 150, 150]
    canv.create_polygon(points, fill = "white", outline = "black")

    # csak eredmeny

    result_label = Label(tl, text = EREDMENY_TEXT.format(""))

    # Placement
    a_label.grid(row = 0, column = 0)
    b_label.grid(row = 1, column = 0)
    c_label.grid(row = 2, column = 0)

    a_entry.grid(row = 0, column = 1)
    b_entry.grid(row = 1, column = 1)
    c_entry.grid(row = 2, column = 1)

    calc_button.grid(row = 3, column = 1, sticky=E)

    geometry_frame.grid(row = 0, column = 0)
    field_frame.grid(row = 0, column = 0)
    canv.grid(row = 0, column = 1, padx = 20, pady = 20)

    result_label.grid(row = 1, column = 0, columnspan = 2, sticky=W)

    tl.configure(padx = 10, pady = 10)
    tl.mainloop()
