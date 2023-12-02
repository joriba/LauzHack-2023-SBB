from enum import Enum


class NoticeAttributeEnum(str, Enum):
    BIKE_TRANSPORT = "BIKE_TRANSPORT"
    COUCHETTE = "COUCHETTE"
    EXCLUDE_TILTING_TRAIN = "EXCLUDE_TILTING_TRAIN"
    GROUPS_ADMITTED = "GROUPS_ADMITTED"
    SLEEPING_CAR = "SLEEPING_CAR"

    def __str__(self) -> str:
        return str(self.value)
