from enum import Enum


class OccupancyAverageEnum(str, Enum):
    ALL = "ALL"
    FIRST_HIGH = "FIRST_HIGH"
    FIRST_LOW = "FIRST_LOW"
    FIRST_MEDIUM = "FIRST_MEDIUM"
    SECOND_HIGH = "SECOND_HIGH"
    SECOND_LOW = "SECOND_LOW"
    SECOND_MEDIUM = "SECOND_MEDIUM"

    def __str__(self) -> str:
        return str(self.value)
