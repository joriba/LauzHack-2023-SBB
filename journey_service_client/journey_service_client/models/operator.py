from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Operator")


@_attrs_define
class Operator:
    """A company providing public transport services (aka Carrier).

    Attributes:
        id (str): DiDok/INFO+/Plabe related operator-number (typically Integer for CH managed codes, however some TU's
            like in foreign countries might return String expressions like '80___'), relates to operatorName.
            NOVA does not accept trimmed numbers! Example: 000011.
        name (Union[Unset, str]): Fullname of responsible operator, relates to operatorNumber. This value matches with
            [OpenTransportData.swiss GoList field
            'BEZEICHNUNG_DE'](https://opentransportdata.swiss/de/dataset/goch).<br>(Translated according to Accept-
            Language.) Example: Schweizerische Bundesbahnen SBB.
        short_name (Union[Unset, str]): Abbreviation of operator, relates to operatorName. This value might differ from
            OpenTransportData.swiss abbreviation (there are 3 different versions, J-S supports 3-digit
            abbreviation).<br>(Translated according to Accept-Language.) Example: SBB.
    """

    id: str
    name: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        short_name = self.short_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if short_name is not UNSET:
            field_dict["shortName"] = short_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name", UNSET)

        short_name = d.pop("shortName", UNSET)

        operator = cls(
            id=id,
            name=name,
            short_name=short_name,
        )

        operator.additional_properties = d
        return operator

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
