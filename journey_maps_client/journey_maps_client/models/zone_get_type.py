from enum import Enum


class ZoneGetType(str, Enum):
    ABO = "ABO"
    TICKET = "TICKET"

    def __str__(self) -> str:
        return str(self.value)
