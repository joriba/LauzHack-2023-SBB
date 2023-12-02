from enum import Enum


class CarType(str, Enum):
    CAR = "CAR"
    CC = "CC"
    FA = "FA"
    FZ = "FZ"
    LOK = "LOK"
    SL = "SL"
    UNKNOWN = "UNKNOWN"
    WL = "WL"
    WR = "WR"

    def __str__(self) -> str:
        return str(self.value)
