from enum import Enum


class GetTripsWithEcoBalanceByReconstructionContextCarFuelType(str, Enum):
    AVG = "AVG"
    DIESEL = "DIESEL"
    ELECTRIC = "ELECTRIC"
    GAS = "GAS"
    HYBRID = "HYBRID"
    LPG = "LPG"
    PLUGIN = "PLUGIN"

    def __str__(self) -> str:
        return str(self.value)
