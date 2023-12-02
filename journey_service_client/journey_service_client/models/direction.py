from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Direction")


@_attrs_define
class Direction:
    """Direction of Vehicle (typically shown on Vehicle-display or Display at Quay).

    Attributes:
        name (str): StopPlace::name or any direction-name. Example: Basel SBB.
        route_index_from (Union[Unset, int]): From relevant StopPoint::routeIndex (might be given for
            JourneyDetail::directions).
        route_index_to (Union[Unset, int]): To relevant StopPoint::routeIndex (might be given for
            JourneyDetail::directions).
    """

    name: str
    route_index_from: Union[Unset, int] = UNSET
    route_index_to: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        route_index_from = self.route_index_from
        route_index_to = self.route_index_to

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if route_index_from is not UNSET:
            field_dict["routeIndexFrom"] = route_index_from
        if route_index_to is not UNSET:
            field_dict["routeIndexTo"] = route_index_to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        route_index_from = d.pop("routeIndexFrom", UNSET)

        route_index_to = d.pop("routeIndexTo", UNSET)

        direction = cls(
            name=name,
            route_index_from=route_index_from,
            route_index_to=route_index_to,
        )

        direction.additional_properties = d
        return direction

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
