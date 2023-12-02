import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="OperatingPeriodSubscription")


@_attrs_define
class OperatingPeriodSubscription:
    """HCSS ServiceDays.

    Attributes:
        operating_days (List[datetime.date]):
        name (str):
    """

    operating_days: List[datetime.date]
    name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operating_days = []
        for operating_days_item_data in self.operating_days:
            operating_days_item = operating_days_item_data.isoformat()
            operating_days.append(operating_days_item)

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operatingDays": operating_days,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        operating_days = []
        _operating_days = d.pop("operatingDays")
        for operating_days_item_data in _operating_days:
            operating_days_item = isoparse(operating_days_item_data).date()

            operating_days.append(operating_days_item)

        name = d.pop("name")

        operating_period_subscription = cls(
            operating_days=operating_days,
            name=name,
        )

        operating_period_subscription.additional_properties = d
        return operating_period_subscription

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
