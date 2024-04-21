
class Item:
    def __init__(self, description, status):
        self.description = description
        self.status = status

    def to_csv(self):
        return f"{self.description}, {self.status}" + "\n"

    def is_valid(self):
        return self.description and self.status in ["pending", "complete"]

