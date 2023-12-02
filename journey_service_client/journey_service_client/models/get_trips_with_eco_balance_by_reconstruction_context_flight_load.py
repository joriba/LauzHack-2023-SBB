from enum import Enum


class GetTripsWithEcoBalanceByReconstructionContextFlightLoad(str, Enum):
    AVG = "AVG"
    FULL = "FULL"

    def __str__(self) -> str:
        return str(self.value)
