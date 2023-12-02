from enum import Enum


class StopV2ExitSide(str, Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
