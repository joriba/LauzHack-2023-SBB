from enum import Enum


class TransportType(str, Enum):
    BOAT = "boat"
    BUS = "bus"
    FUNICULAR = "funicular"
    GONDOLA = "gondola"
    TRAIN = "train"
    TRAM = "tram"

    def __str__(self) -> str:
        return str(self.value)
