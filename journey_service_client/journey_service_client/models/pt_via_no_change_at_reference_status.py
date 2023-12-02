from enum import Enum


class PTViaNoChangeAtReferenceStatus(str, Enum):
    NO_TRANSFER = "NO_TRANSFER"
    NO_TRANSFER_META_STOPPLACE = "NO_TRANSFER_META_STOPPLACE"

    def __str__(self) -> str:
        return str(self.value)
