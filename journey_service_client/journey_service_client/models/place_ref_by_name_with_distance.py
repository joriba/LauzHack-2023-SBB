from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlaceRefByNameWithDistance")


@_attrs_define
class PlaceRefByNameWithDistance:
    """A reference to a stop-place with its distance from the context (parent element). Name is temporary!

    Attributes:
        name (str): Unique non-translated resp. local name of StopPlace. Example: Konstanz.
        distance (Union[Unset, int]): Specifies the distance in [m] from the parent element. Example: 2000.
    """

    name: str
    distance: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        distance = self.distance

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if distance is not UNSET:
            field_dict["distance"] = distance

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        distance = d.pop("distance", UNSET)

        place_ref_by_name_with_distance = cls(
            name=name,
            distance=distance,
        )

        place_ref_by_name_with_distance.additional_properties = d
        return place_ref_by_name_with_distance

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
