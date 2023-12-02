from enum import Enum


class RealtimeModeEnum(str, Enum):
    OFF = "OFF"
    REALTIME = "REALTIME"
    REALTIME_RIDEABLE = "REALTIME_RIDEABLE"

    def __str__(self) -> str:
        return str(self.value)
