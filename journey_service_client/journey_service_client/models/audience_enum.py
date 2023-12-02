from enum import Enum


class AudienceEnum(str, Enum):
    B2C_MAP = "B2C_MAP"
    B2C_TEXT = "B2C_TEXT"
    B2C_TIMETABLE = "B2C_TIMETABLE"
    B2E_MAP = "B2E_MAP"
    B2E_TEXT = "B2E_TEXT"

    def __str__(self) -> str:
        return str(self.value)
