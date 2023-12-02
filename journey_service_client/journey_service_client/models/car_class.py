from enum import Enum


class CarClass(str, Enum):
    VALUE_0 = "1"
    VALUE_1 = "2"
    VALUE_2 = "12"

    def __str__(self) -> str:
        return str(self.value)
