from enum import Enum


class GroupReservationStatusEnum(str, Enum):
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
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
