from enum import Enum


class StopPointModeEnum(str, Enum):
    DEFAULT = "DEFAULT"
    EQUIVALENTS = "EQUIVALENTS"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
