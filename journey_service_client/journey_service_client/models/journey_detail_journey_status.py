from enum import Enum


class JourneyDetailJourneyStatus(str, Enum):
    ADDITIONAL = "ADDITIONAL"
    PLANNED = "PLANNED"
    REPLACEMENT = "REPLACEMENT"
    SPECIAL = "SPECIAL"

    def __str__(self) -> str:
        return str(self.value)
