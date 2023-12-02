from enum import Enum


class Mot(str, Enum):
    BUS = "bus"
    CAR = "car"
    FERRY = "ferry"
    FOOT = "foot"
    FUNICULAR = "funicular"
    GONDOLA = "gondola"
    RAIL = "rail"
    SUBWAY = "subway"
    TRAM = "tram"

    def __str__(self) -> str:
        return str(self.value)
