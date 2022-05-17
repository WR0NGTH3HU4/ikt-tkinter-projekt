from Window import Window

class WindowHandler:

    windows = []

    # direkt nem __init__()
    @staticmethod
    def init():
        pass

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

    @staticmethod
    def run_window(id: str):
        window = WindowHandler.get_window(id)
        window.run()

