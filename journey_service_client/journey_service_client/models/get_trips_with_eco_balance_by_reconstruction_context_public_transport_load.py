from enum import Enum


class GetTripsWithEcoBalanceByReconstructionContextPublicTransportLoad(str, Enum):
    AVG = "AVG"
    FULL = "FULL"

    def __str__(self) -> str:
        return str(self.value)
