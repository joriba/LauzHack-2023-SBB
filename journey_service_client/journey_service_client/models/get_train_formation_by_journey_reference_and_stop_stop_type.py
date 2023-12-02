from enum import Enum


class GetTrainFormationByJourneyReferenceAndStopStopType(str, Enum):
    STATION = "STATION"

    def __str__(self) -> str:
        return str(self.value)
