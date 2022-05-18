# pylint: disable=import-error
from window.window_handler import WindowHandler
import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))

if __name__ == '__main__':
    print("Launched directly")
    WindowHandler.init()
    print(WindowHandler.get_window("test"))
