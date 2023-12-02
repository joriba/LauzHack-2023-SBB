from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BoardingPosition")


@_attrs_define
class BoardingPosition:
    """A location within a `Quay` from which passengers may directly board, or onto which passengers may directly alight
    from a vehicle.

        Attributes:
            id (str): Non-formal id provided by J-S. Example: 8507000_12_C.
            name (str): Boarding/alighting position which could be a concrete track (boardable/alightable by attached
                `Quay`), a section name (aka de:Sektor) or both. Example: C.
    """

    id: str
    name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        boarding_position = cls(
            id=id,
            name=name,
        )

        boarding_position.additional_properties = d
        return boarding_position

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
