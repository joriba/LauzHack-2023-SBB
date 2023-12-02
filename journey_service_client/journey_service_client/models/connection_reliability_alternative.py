from enum import Enum


class ConnectionReliabilityAlternative(str, Enum):
    ABORTIVE = "ABORTIVE"
    GUARANTEED = "GUARANTEED"
    HIGH = "HIGH"
    LOW = "LOW"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
