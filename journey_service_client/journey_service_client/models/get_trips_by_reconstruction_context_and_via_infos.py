from enum import Enum


class GetTripsByReconstructionContextAndViaInfos(str, Enum):
    RN = "RN"

    def __str__(self) -> str:
        return str(self.value)
