from enum import Enum


class V2TripsAttributesItem(str, Enum):
    BIKE_CARRIAGE = "BIKE_CARRIAGE"
    COUCHETTE = "COUCHETTE"
    EXCLUDE_TILTING_TRAIN = "EXCLUDE_TILTING_TRAIN"
    GROUPS_ADMITTED = "GROUPS_ADMITTED"
    SLEEPING_CAR = "SLEEPING_CAR"

    def __str__(self) -> str:
        return str(self.value)
