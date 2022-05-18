class Window:

    def __init__(self, id):
        self.id = id
        self.title = "null"

    def set_title(self, title):
        self.title = title
        return self
    
    def calculate(self):
        raise NotImplementedError()

    def run(self):
        raise NotImplementedError()