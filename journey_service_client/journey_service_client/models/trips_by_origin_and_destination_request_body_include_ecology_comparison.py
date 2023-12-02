from enum import Enum


class TripsByOriginAndDestinationRequestBodyIncludeEcologyComparison(str, Enum):
    DEFAULT = "DEFAULT"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
