from tree import Tree
from apple import Apple


class AppleTree(Tree):
    def __init__(self):
        self.list_of_apples: list[Apple] = []

    def get_an_apple(self) -> Apple:
        return self.list_of_apples.pop()

    def write_name(self, name: str) -> None:
        pass
