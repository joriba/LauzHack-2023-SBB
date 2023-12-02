import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.subscription_period_days_in_week_item import SubscriptionPeriodDaysInWeekItem

T = TypeVar("T", bound="SubscriptionPeriod")


@_attrs_define
class SubscriptionPeriod:
    """Period within the Trip should be observed regularly.

    Attributes:
        begin (datetime.date): First day of a subscription. Example: 2022-04-08.
        end (datetime.date): End of subscription. Use DELETE API to end subscription any time. Example: 2022-06-30.
        days_in_week (List[SubscriptionPeriodDaysInWeekItem]):
    """

    begin: datetime.date
    end: datetime.date
    days_in_week: List[SubscriptionPeriodDaysInWeekItem]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        begin = self.begin.isoformat()
        end = self.end.isoformat()
        days_in_week = []
        for days_in_week_item_data in self.days_in_week:
            days_in_week_item = days_in_week_item_data.value

            days_in_week.append(days_in_week_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "begin": begin,
                "end": end,
                "daysInWeek": days_in_week,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        begin = isoparse(d.pop("begin")).date()

        end = isoparse(d.pop("end")).date()

        days_in_week = []
        _days_in_week = d.pop("daysInWeek")
        for days_in_week_item_data in _days_in_week:
            days_in_week_item = SubscriptionPeriodDaysInWeekItem(days_in_week_item_data)

            days_in_week.append(days_in_week_item)

        subscription_period = cls(
            begin=begin,
            end=end,
            days_in_week=days_in_week,
        )

        subscription_period.additional_properties = d
        return subscription_period

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
