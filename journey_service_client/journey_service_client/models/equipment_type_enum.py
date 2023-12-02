from enum import Enum


class EquipmentTypeEnum(str, Enum):
    WIFI = "WIFI"

    def __str__(self) -> str:
        return str(self.value)
