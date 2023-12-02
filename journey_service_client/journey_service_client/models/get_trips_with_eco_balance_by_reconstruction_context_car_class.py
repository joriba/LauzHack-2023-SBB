from enum import Enum


class GetTripsWithEcoBalanceByReconstructionContextCarClass(str, Enum):
    HIGH_1 = "HIGH_1"
    HIGH_2 = "HIGH_2"
    HIGH_3 = "HIGH_3"
    LOW_1 = "LOW_1"
    LOW_2 = "LOW_2"
    LOW_3 = "LOW_3"
    MEDIUM_1 = "MEDIUM_1"
    MEDIUM_2 = "MEDIUM_2"
    MEDIUM_3 = "MEDIUM_3"
    OFFROAD_1 = "OFFROAD_1"
    OFFROAD_2 = "OFFROAD_2"
    OFFROAD_3 = "OFFROAD_3"
    VAN_1 = "VAN_1"
    VAN_2 = "VAN_2"
    VAN_3 = "VAN_3"

    def __str__(self) -> str:
        return str(self.value)
