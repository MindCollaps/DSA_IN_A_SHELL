from abc import abstractmethod
from game import Player


class Consumable:

    @abstractmethod
    def consume(self, player) -> None:
        pass