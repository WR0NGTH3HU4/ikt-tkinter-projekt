from tkinter import *
from mode import Mode

def teszt_ablak(tk, mode: Mode, nev):
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

    # jobb oldal

    canv = Canvas(geometry_frame, width = 150, height = 150)
    points = [0, 150, 75, 0, 150, 150]
    canv.create_polygon(points, fill = "white", outline = "black")

    # Placement
    a_label.grid(row = 0, column = 0)
    b_label.grid(row = 1, column = 0)
    c_label.grid(row = 2, column = 0)

    a_entry.grid(row = 0, column = 1)
    b_entry.grid(row = 1, column = 1)
    c_entry.grid(row = 2, column = 1)

    geometry_frame.grid(row = 0, column = 0)
    field_frame.grid(row = 0, column = 0)
    canv.grid(row = 0, column = 1, padx = 20, pady = 20)

    tl.mainloop()
