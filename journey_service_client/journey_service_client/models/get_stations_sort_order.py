from enum import Enum


class GetStationsSortOrder(str, Enum):
    NAME = "NAME"
    WEIGHT = "WEIGHT"

    def __str__(self) -> str:
        return str(self.value)
