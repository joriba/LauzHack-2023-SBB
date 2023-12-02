from enum import Enum


class TransportModeEnum(str, Enum):
    BUS = "BUS"
    CABLEWAY_GONDOLA_CHAIRLIFT_FUNICULAR = "CABLEWAY_GONDOLA_CHAIRLIFT_FUNICULAR"
    HIGH_SPEED_TRAIN = "HIGH_SPEED_TRAIN"
    INTERCITY = "INTERCITY"
    INTERREGIO = "INTERREGIO"
    REGIO = "REGIO"
    SHIP = "SHIP"
    SPECIAL_TRAIN = "SPECIAL_TRAIN"
    TRAMWAY = "TRAMWAY"
    URBAN_TRAIN = "URBAN_TRAIN"

    def __str__(self) -> str:
        return str(self.value)
