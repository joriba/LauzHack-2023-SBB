from enum import Enum


class ConnectionReliabilityOriginal(str, Enum):
    ABORTIVE = "ABORTIVE"
    GUARANTEED = "GUARANTEED"
    HIGH = "HIGH"
    LOW = "LOW"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
