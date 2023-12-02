from enum import Enum


class GetTrainStopAssignmentsAcceptLanguage(str, Enum):
    DE = "de"
    EN = "en"
    FR = "fr"
    IT = "it"

    def __str__(self) -> str:
        return str(self.value)
