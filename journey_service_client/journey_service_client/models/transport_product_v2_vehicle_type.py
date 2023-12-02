from enum import Enum


class TransportProductV2VehicleType(str, Enum):
    AIRPLANE = "AIRPLANE"
    BOAT = "BOAT"
    BUS = "BUS"
    CABLEWAY = "CABLEWAY"
    CHAIRLIFT = "CHAIRLIFT"
    COG_RAILWAY = "COG_RAILWAY"
    FUNICULAR = "FUNICULAR"
    LIFT = "LIFT"
    METRO = "METRO"
    TAXI = "TAXI"
    TRAIN = "TRAIN"
    TRAMWAY = "TRAMWAY"

    def __str__(self) -> str:
        return str(self.value)
