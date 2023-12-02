from enum import Enum


class GetRoutesStopBehaviour(str, Enum):
    ALL_BOARDING_ALIGHTING = "ALL_BOARDING_ALIGHTING"
    REAL_BOARDING_ALIGHTING = "REAL_BOARDING_ALIGHTING"

    def __str__(self) -> str:
        return str(self.value)
