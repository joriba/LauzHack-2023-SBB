from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JsonServicePointsInUse")


@_attrs_define
class JsonServicePointsInUse:
    """
    Attributes:
        service_points_in_use (Union[Unset, List[int]]):
    """

    service_points_in_use: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_points_in_use: Union[Unset, List[int]] = UNSET
        if not isinstance(self.service_points_in_use, Unset):
            service_points_in_use = self.service_points_in_use

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_points_in_use is not UNSET:
            field_dict["servicePointsInUse"] = service_points_in_use

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        service_points_in_use = cast(List[int], d.pop("servicePointsInUse", UNSET))

        json_service_points_in_use = cls(
            service_points_in_use=service_points_in_use,
        )

        json_service_points_in_use.additional_properties = d
        return json_service_points_in_use

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
