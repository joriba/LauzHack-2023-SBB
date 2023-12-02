from enum import Enum


class GetTripsByIdAndPartialSearchContextAcceptLanguage(str, Enum):
    DE = "de"
    EN = "en"
    FR = "fr"
    IT = "it"

    def __str__(self) -> str:
        return str(self.value)
