# pylint: disable=import-error
from window.window_handler import WindowHandler
from tkinter import Tk
import threading

# Fekete mágia
import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))
print(sys.modules)


if __name__ == '__main__':
    root = Tk()

    print("Launched directly")
    # WindowHandler.init(root)
