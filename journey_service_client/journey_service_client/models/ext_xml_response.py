from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExtXmlResponse")


@_attrs_define
class ExtXmlResponse:
    """Response with a handle to be used with Hafas::extXML API.

    Attributes:
        xml_handle (str):
        xml_id (str):
        ident_nr (str):
        seq_nr (str):
        con_id (str):
        locale (Union[Unset, str]): @Deprecated IRRELEVANT (just set to 'de' for Swagger2 Client compliance, but there
            is no translation in response)
    """

    xml_handle: str
    xml_id: str
    ident_nr: str
    seq_nr: str
    con_id: str
    locale: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        xml_handle = self.xml_handle
        xml_id = self.xml_id
        ident_nr = self.ident_nr
        seq_nr = self.seq_nr
        con_id = self.con_id
        locale = self.locale

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "xmlHandle": xml_handle,
                "xmlId": xml_id,
                "identNr": ident_nr,
                "seqNr": seq_nr,
                "conId": con_id,
            }
        )
        if locale is not UNSET:
            field_dict["locale"] = locale

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        xml_handle = d.pop("xmlHandle")

        xml_id = d.pop("xmlId")

        ident_nr = d.pop("identNr")

        seq_nr = d.pop("seqNr")

        con_id = d.pop("conId")

        locale = d.pop("locale", UNSET)

        ext_xml_response = cls(
            xml_handle=xml_handle,
            xml_id=xml_id,
            ident_nr=ident_nr,
            seq_nr=seq_nr,
            con_id=con_id,
            locale=locale,
        )

        ext_xml_response.additional_properties = d
        return ext_xml_response

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
