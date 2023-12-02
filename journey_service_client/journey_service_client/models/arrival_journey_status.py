from enum import Enum


class ArrivalJourneyStatus(str, Enum):
    ADDITIONAL = "ADDITIONAL"
    PLANNED = "PLANNED"
    REPLACEMENT = "REPLACEMENT"
    SPECIAL = "SPECIAL"

    def __str__(self) -> str:
        return str(self.value)
