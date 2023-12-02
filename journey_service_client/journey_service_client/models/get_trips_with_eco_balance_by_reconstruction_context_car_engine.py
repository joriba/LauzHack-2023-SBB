from enum import Enum


class GetTripsWithEcoBalanceByReconstructionContextCarEngine(str, Enum):
    AVG = "AVG"
    DIESEL_EURO3 = "DIESEL_EURO3"
    DIESEL_EURO4 = "DIESEL_EURO4"
    DIESEL_EURO5 = "DIESEL_EURO5"
    GAS_EURO3 = "GAS_EURO3"
    GAS_EURO4 = "GAS_EURO4"
    GAS_EURO5 = "GAS_EURO5"
    LPG_CONV = "LPG_CONV"

    def __str__(self) -> str:
        return str(self.value)
