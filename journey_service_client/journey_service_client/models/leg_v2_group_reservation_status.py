from enum import Enum


class LegV2GroupReservationStatus(str, Enum):
    BROKEN = "BROKEN"
    CANCELED = "CANCELED"
    CONFIRMED = "CONFIRMED"
    EMPTY = "EMPTY"
    IGNORED = "IGNORED"
    LOCKED_FOR_GROUPS = "LOCKED_FOR_GROUPS"
    OK = "OK"
    REJECTED = "REJECTED"
    REQUEST_MADE = "REQUEST_MADE"
    REQUEST_POSSIBLE = "REQUEST_POSSIBLE"
    TIMETABLE_DATA_NOT_MATCH = "TIMETABLE_DATA_NOT_MATCH"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
