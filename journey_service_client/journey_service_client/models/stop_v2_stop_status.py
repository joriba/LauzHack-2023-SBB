from enum import Enum


class StopV2StopStatus(str, Enum):
    BEGIN_PARTIAL_CANCELLATION = "BEGIN_PARTIAL_CANCELLATION"
    CANCELLED = "CANCELLED"
    END_PARTIAL_CANCELLATION = "END_PARTIAL_CANCELLATION"
    NOT_SERVICED = "NOT_SERVICED"
    PLANNED = "PLANNED"
    UNPLANNED = "UNPLANNED"

    def __str__(self) -> str:
        return str(self.value)
