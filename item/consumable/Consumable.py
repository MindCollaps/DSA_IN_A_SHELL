from abc import abstractmethod


class Consumable:

    @abstractmethod
    def consume(self, player) -> None:
        pass