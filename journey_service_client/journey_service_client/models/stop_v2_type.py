from enum import Enum


class StopV2Type(str, Enum):
    ADDRESS = "ADDRESS"
    POI = "POI"
    STATION = "STATION"

    def __str__(self) -> str:
        return str(self.value)
