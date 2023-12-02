from enum import Enum


class MessageChannelTypeName(str, Enum):
    MAP_CUSTOMER = "MAP_CUSTOMER"
    MAP_SALE = "MAP_SALE"
    MESSAGELIST_CUSTOMER = "MESSAGELIST_CUSTOMER"
    MESSAGELIST_SALE = "MESSAGELIST_SALE"
    TIMETABLE = "TIMETABLE"

    def __str__(self) -> str:
        return str(self.value)
