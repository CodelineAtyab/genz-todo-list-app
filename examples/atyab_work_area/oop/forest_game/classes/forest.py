from abc import ABC, abstractmethod
from tree import Tree


class Forest(ABC):
    def __init__(self):
        self.list_of_trees: list[Tree] = [Tree()]

    @abstractmethod
    def trees_info(self):
        pass


if __name__ == "__main__":
    Forest()
