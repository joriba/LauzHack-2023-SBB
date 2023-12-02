from enum import Enum


class V2TripsAlternateMatch(str, Enum):
    ALTERNATE_ONLY = "ALTERNATE_ONLY"
    BOTH = "BOTH"
    CANCELLED_ONLY = "CANCELLED_ONLY"
    IRRELEVANT = "IRRELEVANT"

    def __str__(self) -> str:
        return str(self.value)
