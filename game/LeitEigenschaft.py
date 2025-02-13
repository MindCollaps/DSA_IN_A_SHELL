from enum import Enum, auto


def get_leiteigenschaft(player, leiteigenschaft) -> int:
    return player.leit_eigenschaft[leiteigenschaft.value - 1][1]


def set_leiteigenschaft(player, leiteigenschaft, value: int):
    player.leit_eigenschaft[leiteigenschaft.value - 1] = (leiteigenschaft, value)


class LeitEigenschaft(Enum):
    MU = auto()  # Mut
    KL = auto()  # Klugheit
    IN = auto()  # Intuition
    CH = auto()  # Charisma
    FF = auto()  # Fingerfertigkeit
    GE = auto()  # Gewandheit
    KO = auto()  # Konstitution
    KK = auto()  # Koerperkraft
