from enum import Enum


class MessageEdgeDirection(str, Enum):
    BIDIRECTIONAL = "BIDIRECTIONAL"
    OPPOSITE = "OPPOSITE"
    STRAIGHT = "STRAIGHT"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
