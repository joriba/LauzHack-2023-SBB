from enum import Enum


class LegV2FormationHint(str, Enum):
    BOTH = "BOTH"
    BOTH_FORMATION_CHANGE = "BOTH_FORMATION_CHANGE"
    DESTINATION = "DESTINATION"
    DESTINATION_FORMATION_CHANGE = "DESTINATION_FORMATION_CHANGE"
    NONE = "NONE"
    ORIGIN = "ORIGIN"
    ORIGIN_FORMATION_CHANGE = "ORIGIN_FORMATION_CHANGE"

    def __str__(self) -> str:
        return str(self.value)
