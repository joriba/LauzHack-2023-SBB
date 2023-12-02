from enum import Enum


class GetTripsWithEcoBalanceByReconstructionContextCarEuroNorm(str, Enum):
    AVG = "AVG"
    EURO3 = "EURO3"
    EURO4 = "EURO4"
    EURO5 = "EURO5"
    EURO6 = "EURO6"

    def __str__(self) -> str:
        return str(self.value)
