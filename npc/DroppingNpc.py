from abc import abstractmethod

from item import Item


class DroppingNpc:
    def __init__(self):
        pass

    @abstractmethod
    def get_drops(self) -> list[Item]:
        pass
