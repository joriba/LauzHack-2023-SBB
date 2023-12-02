from enum import Enum


class HimMessageV2Category(str, Enum):
    CONSTRUCTION_SITE = "CONSTRUCTION_SITE"
    DELAY = "DELAY"
    DISTURBANCE = "DISTURBANCE"
    END_MESSAGE = "END_MESSAGE"
    INFORMATION = "INFORMATION"
    TRAIN_REPLACEMENT_BY_BUS = "TRAIN_REPLACEMENT_BY_BUS"

    def __str__(self) -> str:
        return str(self.value)
