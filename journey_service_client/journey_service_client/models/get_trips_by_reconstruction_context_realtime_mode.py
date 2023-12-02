from enum import Enum


class GetTripsByReconstructionContextRealtimeMode(str, Enum):
    FULL = "FULL"
    INFOS = "INFOS"
    OFF = "OFF"
    REALTIME = "REALTIME"
    SERVER_DEFAULT = "SERVER_DEFAULT"

    def __str__(self) -> str:
        return str(self.value)
