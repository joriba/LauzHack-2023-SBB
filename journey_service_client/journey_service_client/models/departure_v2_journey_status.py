from enum import Enum


class DepartureV2JourneyStatus(str, Enum):
    ADDITIONAL = "ADDITIONAL"
    PLANNED = "PLANNED"
    REPLACEMENT = "REPLACEMENT"
    SPECIAL = "SPECIAL"

    def __str__(self) -> str:
        return str(self.value)
