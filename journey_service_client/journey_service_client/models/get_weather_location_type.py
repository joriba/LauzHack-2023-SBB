from enum import Enum


class GetWeatherLocationType(str, Enum):
    COORDINATES = "COORDINATES"

    def __str__(self) -> str:
        return str(self.value)
