from enum import Enum


class GetStopPlacesSortOrder(str, Enum):
    DISTANCE = "DISTANCE"
    NAME = "NAME"
    WEIGHT = "WEIGHT"

    def __str__(self) -> str:
        return str(self.value)
