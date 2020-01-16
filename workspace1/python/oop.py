class Student():
    # constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def setId(self, id):
        self.id = id

    def print(self):
        print(f"{self.name} - {self.id}")