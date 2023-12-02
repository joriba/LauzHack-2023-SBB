from enum import Enum


class TripsIntervalByOriginAndDestinationRequestBodyIncludeIntermediateStops(str, Enum):
    ALL = "ALL"
    BOARDING_ALIGHTING = "BOARDING_ALIGHTING"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
