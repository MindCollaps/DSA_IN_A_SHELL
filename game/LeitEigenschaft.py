from enum import Enum, auto

class LeitEigenschaft(Enum):
    MU = auto()
    KL = auto()
    IN = auto()
    CH = auto()
    FF = auto()
    GE = auto()
    KO = auto()
    KK = auto()

    @property
    def name_de(self) -> str:
        return {
            LeitEigenschaft.MU: "Mut",
            LeitEigenschaft.KL: "Klugheit",
            LeitEigenschaft.IN: "Intuition",
            LeitEigenschaft.CH: "Charisma",
            LeitEigenschaft.FF: "Fingerfertigkeit",
            LeitEigenschaft.GE: "Gewandheit",
            LeitEigenschaft.KO: "Konstitution",
            LeitEigenschaft.KK: "Körperkraft"
        }[self]


def get_leiteigenschaft(player, leiteigenschaft: LeitEigenschaft) -> int:
    return next(wert for le, wert in player.leit_eigenschaft if le == leiteigenschaft)

def set_leiteigenschaft(player, leiteigenschaft: LeitEigenschaft, value: int):
    for idx, (le, _) in enumerate(player.leit_eigenschaft):
        if le == leiteigenschaft:
            player.leit_eigenschaft[idx] = (leiteigenschaft, value)
            break