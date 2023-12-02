from enum import Enum


class PointType(str, Enum):
    POINT = "Point"

    def __str__(self) -> str:
        return str(self.value)
