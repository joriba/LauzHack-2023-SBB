from enum import Enum


class GetPlacesByNameTypeItem(str, Enum):
    ADDRESS = "Address"
    ALL = "ALL"
    POINTOFINTEREST = "PointOfInterest"
    STOPPLACE = "StopPlace"

    def __str__(self) -> str:
        return str(self.value)
