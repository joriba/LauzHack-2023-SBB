from enum import Enum


class V2TripsDestinationType(str, Enum):
    ADDRESS_POI = "ADDRESS_POI"
    COORDINATES = "COORDINATES"
    STATION = "STATION"

    def __str__(self) -> str:
        return str(self.value)
