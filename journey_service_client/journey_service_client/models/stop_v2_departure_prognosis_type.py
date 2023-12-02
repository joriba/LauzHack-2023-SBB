from enum import Enum


class StopV2DeparturePrognosisType(str, Enum):
    CALCULATED = "CALCULATED"
    CORRECTED = "CORRECTED"
    MANUAL = "MANUAL"
    PROGNOSED = "PROGNOSED"
    REPORTED = "REPORTED"

    def __str__(self) -> str:
        return str(self.value)
