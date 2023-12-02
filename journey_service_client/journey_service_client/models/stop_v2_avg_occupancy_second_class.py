from enum import Enum


class StopV2AvgOccupancySecondClass(str, Enum):
    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
