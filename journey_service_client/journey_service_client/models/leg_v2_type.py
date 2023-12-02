from enum import Enum


class LegV2Type(str, Enum):
    BIKE_ROUTE = "BIKE_ROUTE"
    CAR_ROUTE = "CAR_ROUTE"
    CHECKIN = "CHECKIN"
    CHECKOUT = "CHECKOUT"
    FOOTPATH = "FOOTPATH"
    PARK_RIDE = "PARK_RIDE"
    PUBLIC_JOURNEY = "PUBLIC_JOURNEY"
    TAXI = "TAXI"
    TELE_TAXI = "TELE_TAXI"
    TRANSFER = "TRANSFER"

    def __str__(self) -> str:
        return str(self.value)
