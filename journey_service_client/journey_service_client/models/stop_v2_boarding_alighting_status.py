from enum import Enum


class StopV2BoardingAlightingStatus(str, Enum):
    ALIGHTING = "ALIGHTING"
    BOARDING = "BOARDING"
    BOARDING_ALIGHTING = "BOARDING_ALIGHTING"
    IRRELEVANT = "IRRELEVANT"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
