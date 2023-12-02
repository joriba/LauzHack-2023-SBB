from enum import Enum


class ExtXmlBodyDocumentLanguage(str, Enum):
    DE = "DE"
    EN = "EN"
    FR = "FR"
    IT = "IT"

    def __str__(self) -> str:
        return str(self.value)
