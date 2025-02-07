from abc import abstractmethod
from enum import Enum
from game import Player

class EffectType(Enum):
    HEAL = 0
    STRENGTH = 1
    DRUNK = 2
    TEXT = 3
    SELF_HARM = 4


class Consumable:
    @abstractmethod
    def consume(self, player) -> [(int|str, EffectType)]:
        pass