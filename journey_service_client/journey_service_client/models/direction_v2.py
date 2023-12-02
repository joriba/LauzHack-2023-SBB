from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DirectionV2")


@_attrs_define
class DirectionV2:
    """Relates to (next) Direction given on KIB/Display at Track or transport-product display.

    Attributes:
        name (Union[Unset, str]): StopV2::name or any direction-name.
        route_index_from (Union[Unset, int]): From relevant StopV2::routeIndex (might be given for
            JourneyDetail::directions).
        route_index_to (Union[Unset, int]): To relevant StopV2::routeIndex (might be given for
            JourneyDetail::directions).
    """

    name: Union[Unset, str] = UNSET
    route_index_from: Union[Unset, int] = UNSET
    route_index_to: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        route_index_from = self.route_index_from
        route_index_to = self.route_index_to

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if route_index_from is not UNSET:
            field_dict["routeIndexFrom"] = route_index_from
        if route_index_to is not UNSET:
            field_dict["routeIndexTo"] = route_index_to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        route_index_from = d.pop("routeIndexFrom", UNSET)

        route_index_to = d.pop("routeIndexTo", UNSET)

        direction_v2 = cls(
            name=name,
            route_index_from=route_index_from,
            route_index_to=route_index_to,
        )

        direction_v2.additional_properties = d
        return direction_v2

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
