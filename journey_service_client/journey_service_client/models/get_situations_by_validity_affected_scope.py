from enum import Enum


class GetSituationsByValidityAffectedScope(str, Enum):
    MAJOR_AREA_DISRUPTION = "MAJOR_AREA_DISRUPTION"

    def __str__(self) -> str:
        return str(self.value)
