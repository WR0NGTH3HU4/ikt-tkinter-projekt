from Window import Window
from .impl.Test import Test #ez nem szép ez nagyon nem

class WindowHandler:

    windows = []

    # direkt nem __init__()
    @staticmethod
    def init():
        WindowHandler.add_window(Test())

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
        window.run()

