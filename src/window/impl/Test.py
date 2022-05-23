import sys
if 'Window' not in sys.modules:
    from ..window_handler import Window

class Test(Window):

    def __init__(self):
        Window.__init__(self, "test")

    def run(self):
        print("xd")
        pass