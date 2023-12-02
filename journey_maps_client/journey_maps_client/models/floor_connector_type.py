from enum import Enum


class FloorConnectorType(str, Enum):
    ELEVATOR = "ELEVATOR"
    ESCALATOR = "ESCALATOR"
    RAMP = "RAMP"
    STAIR = "STAIR"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
