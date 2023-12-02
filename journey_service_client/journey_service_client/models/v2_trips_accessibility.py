from enum import Enum


class V2TripsAccessibility(str, Enum):
    ALL = "ALL"
    BOARDING_ALIGHTING_BY_CREW = "BOARDING_ALIGHTING_BY_CREW"
    BOARDING_ALIGHTING_BY_NOTIFICATION = "BOARDING_ALIGHTING_BY_NOTIFICATION"
    BOARDING_ALIGHTING_SELF = "BOARDING_ALIGHTING_SELF"

    def __str__(self) -> str:
        return str(self.value)
