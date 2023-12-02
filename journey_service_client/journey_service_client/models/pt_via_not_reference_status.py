from enum import Enum


class PTViaNotReferenceStatus(str, Enum):
    NO_PASS_THROUGH = "NO_PASS_THROUGH"
    NO_PASS_THROUGH_META_STOPPLACE = "NO_PASS_THROUGH_META_STOPPLACE"

    def __str__(self) -> str:
        return str(self.value)
