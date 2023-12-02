import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceDaysV2")


@_attrs_define
class ServiceDaysV2:
    """Service-period of a transport-product in regular schedule. Given for a yearly journey-planning period (see /info).

    Attributes:
        operating_days (List[datetime.date]):
        days_regular (Union[Unset, str]): Regular service-days the related transport-product operates on a rather
            'repeatable' scheduled plan.<br>(Translated according to Accept-Language.) Example: täglich.
        days_irregular (Union[Unset, str]): Irregular service-days or exceptions to daysRegular.<br>(Translated
            according to Accept-Language.) Example: nicht 24., 25. Mär, 7., 8. Apr.
        route_index_from (Union[Unset, int]): Related to Stop::routeIndex.
        route_index_to (Union[Unset, int]): Related to Stop::routeIndex.
    """

    operating_days: List[datetime.date]
    days_regular: Union[Unset, str] = UNSET
    days_irregular: Union[Unset, str] = UNSET
    route_index_from: Union[Unset, int] = UNSET
    route_index_to: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operating_days = []
        for operating_days_item_data in self.operating_days:
            operating_days_item = operating_days_item_data.isoformat()
            operating_days.append(operating_days_item)

        days_regular = self.days_regular
        days_irregular = self.days_irregular
        route_index_from = self.route_index_from
        route_index_to = self.route_index_to

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operatingDays": operating_days,
            }
        )
        if days_regular is not UNSET:
            field_dict["daysRegular"] = days_regular
        if days_irregular is not UNSET:
            field_dict["daysIrregular"] = days_irregular
        if route_index_from is not UNSET:
            field_dict["routeIndexFrom"] = route_index_from
        if route_index_to is not UNSET:
            field_dict["routeIndexTo"] = route_index_to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        operating_days = []
        _operating_days = d.pop("operatingDays")
        for operating_days_item_data in _operating_days:
            operating_days_item = isoparse(operating_days_item_data).date()

            operating_days.append(operating_days_item)

        days_regular = d.pop("daysRegular", UNSET)

        days_irregular = d.pop("daysIrregular", UNSET)

        route_index_from = d.pop("routeIndexFrom", UNSET)

        route_index_to = d.pop("routeIndexTo", UNSET)

        service_days_v2 = cls(
            operating_days=operating_days,
            days_regular=days_regular,
            days_irregular=days_irregular,
            route_index_from=route_index_from,
            route_index_to=route_index_to,
        )

        service_days_v2.additional_properties = d
        return service_days_v2

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
