from .impl.Test import Test #ez nem szép ez nagyon nem
from tkinter import *

class Window:
    
    tl = None

    def __init__(self, id):

        self.id = id
        self.title = "null"

        # {id: str, field: Entry}
        self.input_fields: {}

        self.tl = Toplevel(WindowHandler.tk)


    def set_title(self, title):
        self.title = title
        return self
    
    def calculate(self):
        raise NotImplementedError()

    def start(self):
        self.run()
        self.tl.mainloop()

    def run(self):
        raise NotImplementedError()

class WindowHandler:

    tk = None
    windows = []

    # direkt nem __init__()
    @staticmethod
    def init(tk):
        WindowHandler.tk = tk
        WindowHandler.add_window(Test())

        b = Button(WindowHandler.tk, text="xd", command=lambda: WindowHandler.run_window("test"))
        b.pack()

        WindowHandler.tk.mainloop()

    # Window típusú objektumot tudunk hozzáadni a csomópont listájához
    @staticmethod
    def add_window(wi: Window):
        WindowHandler.windows.append(wi)

    # Ez a method visszaadja a megadott inicializált ablakot id alapján
    @staticmethod
    def get_window(id: str):
        for window in WindowHandler.windows:
            if window.id == id:
                return window
        return None

    # Elindítunk egy ablakot
    @staticmethod
    def run_window(id: str):
        window = WindowHandler.get_window(id)
        window.start()

