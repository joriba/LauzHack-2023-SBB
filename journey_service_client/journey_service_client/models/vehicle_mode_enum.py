from enum import Enum


class VehicleModeEnum(str, Enum):
    BUS = "BUS"
    CABLEWAY = "CABLEWAY"
    CHAIRLIFT = "CHAIRLIFT"
    COG_RAILWAY = "COG_RAILWAY"
    ELEVATOR = "ELEVATOR"
    GONDOLA = "GONDOLA"
    METRO = "METRO"
    PLANE = "PLANE"
    SHIP = "SHIP"
    TAXI = "TAXI"
    TRAIN = "TRAIN"
    TRAMWAY = "TRAMWAY"

    def __str__(self) -> str:
        return str(self.value)
