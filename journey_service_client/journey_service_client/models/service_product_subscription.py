from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceProductSubscription")


@_attrs_define
class ServiceProductSubscription:
    """
    Attributes:
        name (str):
        line_or_number (Union[Unset, str]):
        vehicle_sub_mode_short_name (Union[Unset, str]):
    """

    name: str
    line_or_number: Union[Unset, str] = UNSET
    vehicle_sub_mode_short_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        line_or_number = self.line_or_number
        vehicle_sub_mode_short_name = self.vehicle_sub_mode_short_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if line_or_number is not UNSET:
            field_dict["lineOrNumber"] = line_or_number
        if vehicle_sub_mode_short_name is not UNSET:
            field_dict["vehicleSubModeShortName"] = vehicle_sub_mode_short_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        line_or_number = d.pop("lineOrNumber", UNSET)

        vehicle_sub_mode_short_name = d.pop("vehicleSubModeShortName", UNSET)

        service_product_subscription = cls(
            name=name,
            line_or_number=line_or_number,
            vehicle_sub_mode_short_name=vehicle_sub_mode_short_name,
        )

        service_product_subscription.additional_properties = d
        return service_product_subscription

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
