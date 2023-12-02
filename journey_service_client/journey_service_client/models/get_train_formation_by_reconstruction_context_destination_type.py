from enum import Enum


class GetTrainFormationByReconstructionContextDestinationType(str, Enum):
    STATION = "STATION"

    def __str__(self) -> str:
        return str(self.value)
