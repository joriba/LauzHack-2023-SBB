from enum import Enum


class GetTripsWithEcoBalanceByReconstructionContextLoad(str, Enum):
    AVG = "AVG"
    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM = "MEDIUM"

    def __str__(self) -> str:
        return str(self.value)
