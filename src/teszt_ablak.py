from tkinter import *
from mode import Mode

def teszt_ablak(tk, mode: Mode, nev):
    tl = Toplevel(tk)
    tl.title(nev)

    a_label = Label(tl, text = "A: ")
    b_label = Label(tl, text = "B: ")
    c_label = Label(tl, text = "C: ")

    a_entry = Entry(tl)
    b_entry = Entry(tl)
    c_entry = Entry(tl)

    tl.mainloop()
