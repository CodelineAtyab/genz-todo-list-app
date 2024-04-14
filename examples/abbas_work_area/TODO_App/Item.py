class Item:
    def __init__(self, description, status):
        self.description = description
        self.status = status

    def to_csv(self):
        return f"{self.description}, {self.status}" + "\n"
