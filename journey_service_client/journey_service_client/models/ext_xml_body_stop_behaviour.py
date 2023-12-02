from enum import Enum


class ExtXmlBodyStopBehaviour(str, Enum):
    ALL_BOARDING_ALIGHTING = "ALL_BOARDING_ALIGHTING"
    ORIGIN_DESTINATION_ONLY = "ORIGIN_DESTINATION_ONLY"
    REAL_BOARDING_ALIGHTING = "REAL_BOARDING_ALIGHTING"

    def __str__(self) -> str:
        return str(self.value)
