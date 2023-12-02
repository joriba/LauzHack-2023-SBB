from enum import Enum


class StopPlaceClassification(str, Enum):
    COMPLEX = "COMPLEX"
    SIMPLE = "SIMPLE"
    VIRTUAL = "VIRTUAL"
    ZONED = "ZONED"

    def __str__(self) -> str:
        return str(self.value)
