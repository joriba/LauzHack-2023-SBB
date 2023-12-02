from enum import Enum


class GetTripsWithEcoBalanceByReconstructionContextFlightFeeder(str, Enum):
    CAR = "CAR"
    TRAIN = "TRAIN"

    def __str__(self) -> str:
        return str(self.value)
