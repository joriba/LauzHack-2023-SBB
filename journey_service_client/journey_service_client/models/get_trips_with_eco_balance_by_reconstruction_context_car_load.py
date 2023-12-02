from enum import Enum


class GetTripsWithEcoBalanceByReconstructionContextCarLoad(str, Enum):
    AVG = "AVG"
    PASSENGER_1 = "PASSENGER_1"
    PASSENGER_2 = "PASSENGER_2"
    PASSENGER_3 = "PASSENGER_3"
    PASSENGER_4 = "PASSENGER_4"
    PASSENGER_5 = "PASSENGER_5"

    def __str__(self) -> str:
        return str(self.value)
