from enum import Enum


class GetTripsByReconstructionContextInfos(str, Enum):
    RN = "RN"

    def __str__(self) -> str:
        return str(self.value)
