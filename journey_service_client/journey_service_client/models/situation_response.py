from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pt_situation import PTSituation


T = TypeVar("T", bound="SituationResponse")


@_attrs_define
class SituationResponse:
    """Contains a list of situation-messages (source HIM, aka Siri::SituationsStructure).

    Attributes:
        situations (List['PTSituation']):
    """

    situations: List["PTSituation"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        situations = []
        for situations_item_data in self.situations:
            situations_item = situations_item_data.to_dict()

            situations.append(situations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "situations": situations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pt_situation import PTSituation

        d = src_dict.copy()
        situations = []
        _situations = d.pop("situations")
        for situations_item_data in _situations:
            situations_item = PTSituation.from_dict(situations_item_data)

            situations.append(situations_item)

        situation_response = cls(
            situations=situations,
        )

        situation_response.additional_properties = d
        return situation_response

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
