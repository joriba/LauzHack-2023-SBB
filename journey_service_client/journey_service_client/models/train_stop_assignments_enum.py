from enum import Enum


class TrainStopAssignmentsEnum(str, Enum):
    NONE = "NONE"
    ORIGIN = "ORIGIN"
    ORIGIN_DESTINATION = "ORIGIN_DESTINATION"

    def __str__(self) -> str:
        return str(self.value)
