from enum import Enum


class V2TripsInfos(str, Enum):
    RN = "RN"

    def __str__(self) -> str:
        return str(self.value)
