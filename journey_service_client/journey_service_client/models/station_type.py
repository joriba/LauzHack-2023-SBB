from enum import Enum


class StationType(str, Enum):
    STATION = "STATION"
    STATION_COMPLEX = "STATION_COMPLEX"
    STATION_VIRTUAL = "STATION_VIRTUAL"
    STATION_ZONED = "STATION_ZONED"

    def __str__(self) -> str:
        return str(self.value)
